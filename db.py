# db.py
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='sync',
        password='superjoin',
        database='superJoin'
    )

def insert_db(column1, column2, column3):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sync_table (column1, column2, column3) VALUES (%s, %s, %s)", (column1, column2, column3))
    conn.commit()
    cursor.close()
    conn.close()

def update_db(id, column1, column2, column3):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE sync_table SET column1=%s, column2=%s, column3=%s WHERE id=%s", (column1, column2, column3, id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_db(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sync_table WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def read_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sync_table")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
