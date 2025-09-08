import math

#vraag de gebruiker naar de radius
radius = float(input("Enter the radius of the circle: "))

#bereken de oppervlakte
area = math.pi * radius ** 2

#laat de oppervlakte zien afgerond op 2 decimalen
print(f"The area of the circle with radius {radius:.2f} is {area:.2f}")