import cx_Oracle

# Replace these values with your actual database connection details
db_user = 'your_username'
db_password = 'your_password'
db_host = 'your_database_host'
db_port = 'your_database_port'
db_service_name = 'your_service_name'

# Construct the DSN (Data Source Name)
dsn = cx_Oracle.makedsn(db_host, db_port, service_name=db_service_name)

# Connect to the Oracle database
connection = cx_Oracle.connect(user=db_user, password=db_password, dsn=dsn)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Perform database operations
# Example: Execute a simple query
sql = "SELECT * FROM your_table"
cursor.execute(sql)

# Fetch and print the result
for row in cursor.fetchall():
    print(f"Column1: {row[0]}, Column2: {row[1]}")

# Close cursor and connection
cursor.close()
connection.close()
