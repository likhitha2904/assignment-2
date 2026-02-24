def factorial_number(n):
    if n < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_term(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def sumOfDigits(n): 
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total

def reverseNumber(n):
    sign = -1 if n < 0 else 1
    reversed_value = str(abs(n))[::-1]
    return sign * int(reversed_value)

def isArmstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return n == total

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // calculate_gcd(a, b)

def check_perfect_number(n):
    if n <= 1:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n


def mathMenu():   #menu system
    while True:

        print("\nMATH MENU")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = input("Choose option: ")

        if choice == "10":
            print("Exiting program...")
            break

        try:

            if choice == "1":
                n = int(input("Enter n: "))
                print("Result:", factorial_number(n))

            elif choice == "2":
                n = int(input("Enter n: "))
                print("Prime?", check_prime(n))

            elif choice == "3":
                n = int(input("Enter n: "))
                print("Fibonacci:", fibonacci_term(n))

            elif choice == "4":
                n = int(input("Enter n: "))
                print("Sum of digits:", sumOfDigits(n))

            elif choice == "5":
                n = int(input("Enter n: "))
                print("Reversed:", reverseNumber(n))

            elif choice == "6":
                n = int(input("Enter n: "))
                print("Armstrong?", isArmstrong(n))

            elif choice == "7":
                a = int(input("Enter a: "))
                b = int(input("Enter b: "))
                print("GCD:", calculate_gcd(a, b))

            elif choice == "8":
                a = int(input("Enter a: "))
                b = int(input("Enter b: "))
                print("LCM:", calculate_lcm(a, b))

            elif choice == "9":
                n = int(input("Enter n: "))
                print("Perfect number?", check_perfect_number(n))

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input. Please enter integers only.")

#final call
mathMenu()
