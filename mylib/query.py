"""Query the database"""

import sqlite3


def read_query():
    """Query the database for the top 5 rows of the Murder2015 table"""
    conn = sqlite3.connect("Murder2015.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Murder2015")
    print("Top 5 rows of the Murder2015 table:")
    print(cursor.fetchall())
    conn.close()
    return "Read Success"


def update_query():
    conn = sqlite3.connect("Murder2015.db")
    cursor = conn.cursor()
    # update execution
    cursor.execute("UPDATE Murder2015 SET change = 60 WHERE city = 'Chicago' ")
    conn.commit()
    conn.close()
    return "Update Success"


def delete_query():
    conn = sqlite3.connect("Murder2015.db")
    cursor = conn.cursor()
    # delete execution
    cursor.execute("DELETE FROM Murder2015 WHERE city = 'Chicago'")
    conn.commit()
    conn.close()
    return "Delete Success"


def sorting_Change():
    # Connect to the database
    conn = sqlite3.connect("Murder2015.db")
    cursor = conn.cursor()

    # Execute SQL query
    query = """
    SELECT state, city
    FROM Murder2015
    ORDER BY change;
    """
    cursor.execute(query)
    # Fetch results
    results = cursor.fetchall()
    # Close connection
    conn.commit()
    conn.close()
    print(results)
    return "Sort Success"


if __name__ == "__main__":
    read_query()
    update_query()
    delete_query()
    sorting_Change()
