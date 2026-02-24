
import math   # using math for sqrt (could also use exponent 0.5)

try:
    num_input = input("Enter a number: ")
    num = int(num_input)
except ValueError:
    print("Invalid input.")
    quit()


if num <= 1:
    print(f"{num} is NOT a prime number.")

elif num == 2:
    print("2 is a PRIME number.")

else:
    prime_status = True   # assuming prime first

    limit = int(math.sqrt(num)) + 1   # storing limit separately

    for d in range(2, limit):
        if num % d == 0:
            prime_status = False
            break  

    if prime_status:
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")

try:
    start_input = input("\nEnter start range: ")
    end_input = input("Enter end range: ")

    start = int(start_input)
    end = int(end_input)

    if start > end:
        raise ValueError("Start range must be <= end range.")

except ValueError as err:
    print("Invalid range:", err)
    quit()


print("\nPrime numbers:", end=" ")

for n in range(start, end + 1):

    if n <= 1:
        continue   # skipping 0, 1 and negatives

    is_prime_range = True

    check_limit = int(math.sqrt(n)) + 1

    for d in range(2, check_limit):
        if n % d == 0:
            is_prime_range = False
            break

    if is_prime_range:
        print(n, end=", ")

print()