gender = input("Are you a male or female? ")


if gender.lower() == "male":
    hemoglobin_level = float(input("Enter your hemoglobin level (g/L): "))

    if hemoglobin_level < 134:
        print("\nHemoglobin level too low.")
    elif 134 <= hemoglobin_level <= 167:
        print("\nHemoglobin level normal.")
    elif hemoglobin_level > 167:
        print("\nHemoglobin level too high.")

elif gender.lower() == "female":
    hemoglobin_level = float(input("Enter your hemoglobin level (g/L): "))

    if hemoglobin_level < 117:
        print("\nHemoglobin level too low.")
    elif 117 <= hemoglobin_level <= 155:
        print("\nHemoglobin level normal.")
    elif hemoglobin_level > 155:
        print("\nHemoglobin level too high.")

else:
    print("\nPlease enter a valid gender.")