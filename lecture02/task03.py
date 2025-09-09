#vraag de gebruiker naar de lengte en breedte van de rechthoek
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

#bereken de oppervlakte en omtrek
area = length * width
perimeter = 2 * (length + width)

#laat de berekeningen zien
print(f"\nThe area of the rectangle is: {area:.2f}.")
print(f"The perimeter of the rectangle is: {perimeter:.2f}.")