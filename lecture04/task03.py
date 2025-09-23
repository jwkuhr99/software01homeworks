def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or enter nothing to finish): ")
        if user_input == "":
            break
        number = float(user_input)
        numbers.append(number)

    if numbers:
        print(f"Smallest number entered: {min(numbers)}")
        print(f"Largest number entered: {max(numbers)}")
    else:
        print("No numbers entered")

find_min_max()