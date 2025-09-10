print("This code converts inches to centimeters.")
print("Will stop at negatives.")

while True:
    inches = float(input("\nLength in inches: "))
    if inches < 0:
        print("\nStopped the conversion.")
        break
    centimeters = inches * 2.54
    print(f"{centimeters:.2f} cm")