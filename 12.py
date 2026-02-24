try:
    num_input = input("Enter number: ")
    number = int(num_input)

    range_input = input("Enter range (end): ")
    limit = int(range_input)

    if limit <= 0:
        raise ValueError("Range must be positive.")

except ValueError as err:
    print("Invalid input:", err)
    quit()  


print(f"\nMultiplication Table of {number}\n")

for i in range(1, limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")

#tried bonus
bonus = input("\nGenerate full 1-10 table grid? (yes/no): ")
bonus = bonus.strip().lower()

if bonus == "yes":

    print("\nFull Multiplication Table (1-10)\n")

    # Creating a 10x10 grid
    for r in range(1, 11):
        for c in range(1, 11):

            value = r * c   # storing temporarily
            print(f"{value:4}", end="")

        print()  # move to next line