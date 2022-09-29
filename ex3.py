from geopy import distance
mycursor = connection.cursor()
icao1 = input("Input the first ICAO code: ")
mycursor.execute(f"select name from airport_new where ident = '{icao1}';")
result = mycursor.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
icao2 = input("Input the second ICAO code: ")
mycursor.execute(f"select name from airport_new where ident = '{icao2}';")
result = mycursor.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
mycursor.execute(f"select latitude_deg, longitude_deg from airport_new where ident = '{icao1}' or ident = '{icao2}';")
list = []
for x in mycursor:
    list.append(x)
print(f"The distance between 2 airports is", f"{distance.distance(list[0], list[1]).km:.2f} km")