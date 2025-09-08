#vraag de gebruiker naar 3 integers
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
num3 = int(input("Give me the third number: "))

#bereken het totaal, het product en het gemiddelde
total = num1 + num2 + num3
product = num1 * num2 * num3
average = total/3

#laat de resultaten zien
print(f"The total of the numbers is: {total:.0f}.")
print(f"The product of the numbers is: {product:.0f}.")
print(f"The average of the numbers is: {average:.0f}.")
