import pyodbc

def connect_to_database(server, database, username, password):
    try:
        # Define the connection string
        connection_string = f"DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"

        # Establish a connection
        connection = pyodbc.connect(connection_string)

        print("Connected to the database.")

        # Return the connection object
        return connection

    except pyodbc.Error as ex:
        print(f"Error connecting to the database: {ex}")
        return None

def close_connection(connection):
    try:
        # Close the connection
        connection.close()
        print("Connection closed.")

    except pyodbc.Error as ex:
        print(f"Error closing the connection: {ex}")

# Replace these with your database credentials
server_name = 'your_server_name'
database_name = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Connect to the database
connection = connect_to_database(server_name, database_name, username, password)

# Perform database operations here...

# Close the connection when done
close_connection(connection)
