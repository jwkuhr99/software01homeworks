length = float(input("So you caught a zander? Good job!!! Tell me the length of the fish in centimeters, to see if you can legally keep it: "))

legal_size_limit = 42

if length >= 42:
    print("\nSuch a good catch! You can keep this one!")
else:
    size_difference = legal_size_limit - length
    print(f"\nSorry, but it's too small! It's {size_difference:.2f}c short of the legal size limit. Release it and try again!")