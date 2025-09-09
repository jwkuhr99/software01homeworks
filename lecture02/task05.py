#vraag de gebruiker om talents, pounds en lots
talents = float(input("Enter the number of talents (leiviskä): "))
pounds = float(input("Enter the number of pounds (naula): "))
lots = float(input("Enter the number of lots (luoti): "))

#conversions
pounds_in_talents = 20
lots_in_pounds = 32
grams_in_lots = 13.3

#bereken het totaal in lots
total_lots = (talents * pounds_in_talents * lots_in_pounds) + (pounds * lots_in_pounds) + lots

#bereken het totaal in gram
total_grams = total_lots * grams_in_lots

#bereken de resultaten om in kilogram en de rest in gram
kilograms = int(total_grams / 1000)
grams = round(total_grams % 1000 , 2)

#laat de resultaten zien
print(f"The weight in modern units is {kilograms} kilograms and {grams} grams")