#different functions, trying to create as many functions as possible.
def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def modulus_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b


def power_numbers(a, b):
    # Using exponent operator directly
    return a ** b

#main calculator function
def runCalculator():
    while True:
        print("\nCALCULATOR MENU")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        user_choice = input("Choose option: ")

        if user_choice == "7":
            print("Exiting calculator.")
            break

        if user_choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice.")
            continue

        try:
            first_input = input("Enter first number: ")
            second_input = input("Enter second number: ")

            num1 = float(first_input)
            num2 = float(second_input)

        except ValueError:
            print("Invalid number.")
            continue

        # Mapping choices to functions
        ops = {
            "1": add_numbers,
            "2": subtract_numbers,
            "3": multiply_numbers,
            "4": divide_numbers,
            "5": modulus_numbers,
            "6": power_numbers
        }
        result_value = ops[user_choice](num1, num2)
        print("Result:", result_value)

#call
runCalculator()
