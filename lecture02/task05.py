talents = int(input("Enter the number of talents (leiviskä): "))
pounds = int(input("Enter the number of pounds (naula): "))
lots = int(input("Enter the number of lots (luoti): "))

pounds_in_talents = 20
lots_in_pounds = 32
grams_in_lots = 13.3

total_lots = (talents * pounds_in_talents * lots_in_pounds) + (pounds * lots_in_pounds) + lots

total_grams = total_lots * grams_in_lots

kilograms = int(total_grams / 1000)
grams = round(total_grams % 1000)

print(f"The weight in modern units is {kilograms} kilograms and {grams:.2f} grams")