import math

# Function that calculates the unit price (€/m²) of a pizza
def unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100     # convert radius to meters
    area_m2 = math.pi * radius_m**2        # area of the pizza in square meters
    return price_eur / area_m2             # euros per square meter

# Main program
def main():
    print("Pizza 1:")
    d1 = float(input("Enter diameter (cm): "))
    p1 = float(input("Enter price (€): "))

    print("\nPizza 2:")
    d2 = float(input("Enter diameter (cm): "))
    p2 = float(input("Enter price (€): "))

    up1 = unit_price(d1, p1)
    up2 = unit_price(d2, p2)

    print(f"\nPizza 1 unit price: {up1:.2f} €/m²")
    print(f"Pizza 2 unit price: {up2:.2f} €/m²")

    if up1 < up2:
        print("\nPizza 1 gives better value for money.")
    elif up2 < up1:
        print("\nPizza 2 gives better value for money.")
    else:
        print("\nBoth pizzas have identical value for money.")

# Run the program
main()