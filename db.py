import mysql.connector

# Connect to the database
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='sync',
        password='superjoin',
        database='superJoin'
    )

# Read data from database
def read_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM sync_table')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Insert data into database
def insert_db(column1, column2, column3):
    conn = get_db_connection()
    cursor = conn.cursor()
    insert_query = 'INSERT INTO sync_table (column1, column2, column3) VALUES (%s, %s, %s)'
    cursor.execute(insert_query, (column1, column2, column3))
    conn.commit()
    conn.close()

# Update data in database
def update_db(column1, column2, column3, row_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    update_query = 'UPDATE sync_table SET column1 = %s, column2 = %s, column3 = %s WHERE id = %s'
    cursor.execute(update_query, (column1, column2, column3, row_id))
    conn.commit()
    conn.close()

# Delete data from database
def delete_db(row_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete_query = 'DELETE FROM sync_table WHERE id = %s'
    cursor.execute(delete_query, (row_id,))
    conn.commit()
    conn.close()
