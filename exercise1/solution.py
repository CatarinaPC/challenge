import sqlite3
from tabulate import tabulate

try:
    # Connect to the database
    conn = sqlite3.connect("exercise1.db")
    cur = conn.cursor()

    # Create table and insert data
    with open("create_database.sql", "r") as f:
        cur.executescript(f.read())

    # Execute query
    with open("query.sql", "r") as f:
        query = f.read()
        cur.execute(query)
        rows = cur.fetchall()

    # Extract column names from the result for table headers
    headers = [desc[0] for desc in cur.description]

    # Print the result using the 'tabulate' library
    print("Result:")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    # Close database connection
    conn.close()

except Exception as e:
    print(f"Error occurred: {e}")
