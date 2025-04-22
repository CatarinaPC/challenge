import re
import multiprocessing
from collections import Counter
import traceback
import argparse

"""
Reads all lines from a given text file path.

Args:
    file_path (str): The path to the input text file.

Returns:
    list: A list where each element is a line from the text file.
"""
def read_lines(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

"""
Distributes the lines into approximately n_chunks sub-lists.

Args:
    lines (list): A list of strings (lines from the input text file).
    n_chunks (int): The number of chunks to divide the lines into.

Returns:
    list: A list of lists, where each element of the list is a chunk of lines.
"""
def get_chunks(lines, n_chunks=10):
    
    chunk_size = len(lines) // n_chunks

    chunks = []
    start = 0
    for i in range(n_chunks - 1):
        end = start + chunk_size
        chunks.append(lines[start:end])
        start = end
    
    # last worker will get extra rows if the remainder of the chunk size division is not zero
    chunks.append(lines[start:])

    return chunks

"""
Counts the occurrences of each word in a list of lines.

Args:
    lines (list): A list of strings (lines to process).

Returns:
    Counter: A Counter object where the keys are words (lowercase) and the values are their corresponding counts.
"""
def get_word_counts(lines):

    word_counts = Counter()

    for line in lines:
        words = re.findall(r"\b\w+(?:[-']\w+)*\b", line.lower())
        word_counts.update(words)
    
    return word_counts

"""
Writes the resulting word counts to a given output file, ordered by descending frequency.

Args:
    word_counts (Counter): A Counter object containing word counts.
    file_path (str): The path to the output text file.
"""
def write_file(word_counts, file_path):
    with open(file_path, "w") as file:
        file.write("".join(f"{word} {count}\n" for word, count in word_counts.most_common()))


"""
Reads an input file, processes the counting of word occurences in parallel, and writes the results to an output file.

Args:
    input_file_path (str): The path to the input text file.
    output_file_path (str): The path to the output text file for word counts.
    n_workers (int): The number of worker processes to use for parallel processing. Must be a positive integer.
"""
def parallel_threads(input_file_path, output_file_path, n_workers=10):

    try:

        if n_workers <= 0:
            raise ValueError("n_workers must be a positive integer")

        lines = read_lines(input_file_path)

        n_workers = min(n_workers, len(lines)) # considering the case where n_workers > len(lines), this avoids workers having no lines to process
        
        chunks = get_chunks(lines, n_workers)

        with multiprocessing.Pool(processes=n_workers) as pool:
            word_counts_by_worker = pool.map(get_word_counts, chunks)

        final_counts = Counter()
        for counts in word_counts_by_worker:
            final_counts.update(counts)

        write_file(final_counts, output_file_path)
    
    except FileNotFoundError as e:
        print(f"Error occured: input file not found at '{input_file_path}")
    except PermissionError as e:
        print(f"Error occured: permission denied error: {e}")
    except UnicodeDecodeError as e:
        print(f"Error occured: encoding issue while accessing the file {e}")
    except multiprocessing.ProcessError as e:
        print(f"Error occored: error in a worker process {e}")
    except ValueError as e:
        print(f"Error occured: value error {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description="Obtain the number of occurences of each word in input text and save the result to output file with the computation being distributed. Use text.txt as an input text file if you wish.")
    parser.add_argument("input_file", help="Path to the input text file.")
    parser.add_argument("output_file", help="Path to the output result file.")
    parser.add_argument("-w", "--n_workers", type=int, default=10, help="Number of worker processes (default: 10). Must be a positive integer.")

    args = parser.parse_args()

    parallel_threads(args.input_file, args.output_file, args.n_workers)
