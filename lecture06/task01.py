seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of the month (1-12): "))

if 1 <= month <= 12:
    season_index = ((month % 12) // 3)
    print(seasons[season_index])
else:
    print("Invalid month. Please enter a number between 1 and 12.")