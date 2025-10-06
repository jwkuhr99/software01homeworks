def airport_program():
    airports = {}

    while True:
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. Fetch information of an existing airport")
        print("3. Quit the program")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            icao = input("Enter ICAO code: ").strip().upper()
            name = input("Enter airport name: ").strip()
            airports[icao] = name
            print("Airport saved!")

        elif choice == '2':
            icao = input("Enter ICAO code to fetch: ").strip().upper()
            if icao in airports:
                print(f"{icao}: {airports[icao]}")
            else:
                print("Airport not found.")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

airport_program()