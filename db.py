import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='sync',
            password='superjoin',
            database='superJoin'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Read data from database
def read_db():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM sync_table')
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error reading from DB: {e}")
        finally:
            cursor.close()
            conn.close()

# Insert data into database
def insert_db(id, column1, column2, column3):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            insert_query = 'INSERT INTO sync_table (id, column1, column2, column3) VALUES (%s, %s, %s, %s)'
            cursor.execute(insert_query, (id, column1, column2, column3))
            conn.commit()
        except Error as e:
            print(f"Error inserting into DB: {e}")
        finally:
            cursor.close()
            conn.close()

# Update data in database
def update_db(column1, column2, column3, row_id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            UPDATE sync_table
            SET column1 = %s, column2 = %s, column3 = %s
            WHERE id = %s
            """
            cursor.execute(query, (column1, column2, column3, row_id))
            conn.commit()
        except Error as e:
            print(f"Error updating DB: {e}")
        finally:
            cursor.close()
            conn.close()

# Delete data from database
def delete_db(row_id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            delete_query = 'DELETE FROM sync_table WHERE id = %s'
            cursor.execute(delete_query, (row_id,))
            conn.commit()
        except Error as e:
            print(f"Error deleting from DB: {e}")
        finally:
            cursor.close()
            conn.close()
