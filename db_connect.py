import psycopg2

conn = psycopg2.connect(database="probe_management_system", user = "postgres", password = "nikhil", host = "127.0.0.1", port = "5432")

print("Opened database successfully")