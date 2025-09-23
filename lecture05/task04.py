cities = []

print("Enter 5 city names")
for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities.append(city)

print("You entered these cities:")
for city in cities:
    print(city)