from tabulate import tabulate
import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3307,
    database='flight_game',
    user='root',
    password='maria-metro',
    autocommit= True)
icao = input("Please input ICAO code: ")
mycursor = connection.cursor()
mycursor.execute(f"select name as 'airport name', municipality as 'location' from airport_new where ident = '{icao}';")
result = mycursor.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
print(mycursor.rowcount, 'rows in set')