cabin_class = input("Enter you cabin class to receive a description: ")

if cabin_class.lower() == "lux":
    print("\nUpper-deck cabin with a balcony.")
elif cabin_class.lower() == "a":
    print("\nCabin above the car deck with a window.")
elif cabin_class.lower() == "b":
    print("\nWindowless cabin above the car deck.")
elif cabin_class.lower() == "c":
    print("\nWindowless cabin below the car deck.")
else:
    print("\nInvalid cabin class.")