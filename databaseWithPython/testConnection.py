import mysql.connector

def test_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yosef@6607???",
            database="studydatabase"
        )
        if conn.is_connected():
            table_name = input("Enter table name: ")
            column_name = input("Enter column name: ")
            query = f"SELECT {column_name} FROM {table_name}"
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            cursor.close
            conn.close()
    except mysql.connector.Error as e:
        print(f"Connection error: {e}")

test_connection()






