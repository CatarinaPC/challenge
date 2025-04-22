# Sword Health's Technical Challenge

This project contains a folder with the solution for each exercise in the presented technical challenge.

## Getting Started

1.  **Prerequisites:**
    * Python 3.x installed

2.  **Installation:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate  # On Windows
    pip install -r requirements.txt
    ```

## Usage

1.  **Excercise 1**
    * Assuming you're in the exercise1 folder, run the script from your terminal with:
        ```bash
        python solution.py
        ```

2.  **Exercise 2**
    * Assuming you're in the exercise2 folder, run the script from your terminal with:
        ```bash
        python solution.py text.txt result.txt -w 10
        ```
    * Arguments:
        * `input_file`:
            * **Required:** Yes
            * **Description:** Path to the text file to process. You can use text.txt to test.

        * `output_file`:
            * **Required:** Yes
            * **Description:** Path to the file the results will be saved.

        * `-w`, `--n_workers`:
            * **Required:** No (Optional)
            * **Type:** Integer
            * **Default:** `10`
            * **Description:** The number of worker processes to use for parallel processing. Must be a positive integer.


## Project Structure
    .
    ├── exercise1
        ├── create_database.sql     # script that creates the table and inserts data
        ├── query.sql               # script that contains the solution query
        ├── solution.py             # script that creates database, runs query and prints the result
    ├── exercise2
        ├── solution.py             # script with the solution of the exercise  
        ├── text.txt                # example test file to use as input for solution.py
    ├── README.md                   
    ├── requirements.txt
