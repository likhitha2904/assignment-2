try:
    raw_input_number = input("Enter a number: ")
    num = int(raw_input_number)

except ValueError:
    print("Invalid input! Please enter an integer.")
    quit()

#factorial
if num < 0:
    print("Factorial is not defined for negative numbers.")

elif num == 0:
    # Special case
    print("0! = 1")

else:
    fact = 1
    steps = ""   # building string manually

    # Loop from num down to 1
    for i in range(num, 0, -1):

        fact = fact * i  

        steps += str(i)

        if i != 1:
            steps += "x"

    # Printing result
    print(f"{num}! = {steps} = {fact}")