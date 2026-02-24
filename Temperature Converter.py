def showMenu():   #main menu
    print("\nTEMPERATURE CONVERTER ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

running = True   # using a flag 

while running:

    showMenu()

    # Getting menu choice
    try:
        choice_raw = input("Enter your choice (1-7): ")
        userChoice = int(choice_raw)
    except ValueError:
        print("Invalid choice! Please enter a number between 1 and 7.")
        continue

    # Exit condition
    if userChoice == 7:
        print("Exiting program. Thank you!")
        running = False
        break

    # Range validation
    if userChoice < 1 or userChoice > 7:
        print("Invalid choice! Please select between 1 and 7.")
        continue

    # Getting temperature value
    try:
        temp_input = input("Enter temperature value: ")
        tempValue = float(temp_input)
    except ValueError:
        print("Invalid temperature input! Please enter a numeric value.")
        continue


    # Keeping formulas directly here instead of separate functions
    if userChoice == 1:
        # Celsius to Fahrenheit
        result = (tempValue * 9/5) + 32
        print(f"Result: {result:.2f} °F")

    elif userChoice == 2:
        # Fahrenheit to Celsius
        result = (tempValue - 32) * 5/9
        print(f"Result: {result:.2f} °C")

    elif userChoice == 3:
        # Celsius to Kelvin
        result = tempValue + 273.15
        print(f"Result: {result:.2f} K")

    elif userChoice == 4:
        # Kelvin to Celsius
        result = tempValue - 273.15
        print(f"Result: {result:.2f} °C")

    elif userChoice == 5:
        # Fahrenheit to Kelvin
        # Doing it step-by-step
        celsius_temp = (tempValue - 32) * 5/9
        result = celsius_temp + 273.15
        print(f"Result: {result:.2f} K")

    elif userChoice == 6:
        # Kelvin to Fahrenheit
        celsius_temp = tempValue - 273.15
        result = (celsius_temp * 9/5) + 32
        print(f"Result: {result:.2f} °F")

    print("-" * 35)
