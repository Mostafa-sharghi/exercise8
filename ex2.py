areaCode = input("Input the area code (i.e. FI): ").upper()
mycursor = connection.cursor()
mycursor.execute(f"select country.name as 'country name', airport_new.name as 'airport name', airport_new.type as 'airport type' from country, airport_new where country.iso_country = airport_new.iso_country and airport_new.iso_country = '{areaCode}' order by airport_new.type;")
result = mycursor.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
print(mycursor.rowcount, 'rows in set')