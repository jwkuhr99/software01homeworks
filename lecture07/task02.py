# Function that converts gallons to litres
def gallons_to_litres(gallons):
    return gallons * 3.78541  # 1 US gallon = 3.78541 litres

# Main program
def main():
    while True:
        gallons = float(input("Enter amount in gallons (negative value to stop): "))

        if gallons < 0:
            print("Program stopped.")
            break

        litres = gallons_to_litres(gallons)
        print(f"{gallons} gallons is equal to {litres:.2f} litres.\n")

# Run the program
main()