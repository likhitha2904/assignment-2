#used try-except to ensure right input
try:
    number1 =float(input("enter first number"))
    number2 =float(input("enter first number"))

except ValueError:
    print("inclid input, onlu number are allowed :(")
    exit() #stops the execution of the program

add_result= number1 +number2
sub_result= number1 - number2
mul_result= number1 *number2
exponential_result=number1**number2

#division by zero error
if number2 !=0:
    div_result=number1/number2
    mod_result=number1%number2
else:
    div_result="cannot divide by 0"
    mod_result="cannot divide by 0"

print("\nResults:")
print(f"{number1} + {number2} = {add_result}")
print(f"{number1} - {number2} = {sub_result}")
print(f"{number1} x {number2} = {mul_result}")
print(f"{number1} ^ {number2} = {exponential_result}")
print(f"{number1} / {number2} = {div_result:.2f}") #2 decimal places only
print(f"{number1} % {number2} = {mod_result}")