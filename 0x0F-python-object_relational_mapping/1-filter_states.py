#!/usr/bin/python3
import MySQLdb
import sys

def list_states_starting_with_N(username, password, database_name):
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states_starting_with_N(username, password, database_name)

