import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve states sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
