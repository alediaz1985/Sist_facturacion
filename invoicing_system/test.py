import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432",
        database="postgres"
    )
    cursor = connection.cursor()
    print("Conexión exitosa")
    cursor.close()
    connection.close()
except Exception as e:
    print("Error durante la conexión:", e)