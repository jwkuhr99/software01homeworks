length = float(input("You caught a zander, good job!!! Tell me the length of the fish in centimeters, to see if you can legally keep it: "))

legal_size_limit = 42

if length >= 42:
    print("\nSuch a good catch! You can keep this one!")
else:
    size_difference = legal_size_limit - length
    print(f"\nAhh sorry, it's too small! It's {size_difference:.2f} centimeters short to the size limit. Release it and try again!")