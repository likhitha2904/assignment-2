try:
    raw_year = input("Enter a year: ")
    year_value = int(raw_year)

    if year_value <= 0:
        raise ValueError("Year must be a positive integer.")

except ValueError as err:
    print("Invalid input:", err)
    quit() 

# Divisible by 4
# Not divisible by 100 UNLESS also divisible by 400

isLeap = False   # assume not leap initially

if year_value % 4 == 0:
    if year_value % 100 == 0:
        if year_value % 400 == 0:
            isLeap = True
        else:
            isLeap = False
    else:
        isLeap = True
else:
    isLeap = False

#reasoning
if isLeap:
    status_text = "Leap Year"

    if year_value % 400 == 0:
        explanation = "It is divisible by 400, which makes it a leap year."
    elif year_value % 100 == 0:
        # Technically this branch won't happen because of logic above, but leaving it here for readability.
        explanation = "It is divisible by 100 but also divisible by 400."
    else:
        explanation = "It is divisible by 4 and not divisible by 100."

else:
    status_text = "NOT a Leap Year"

    if year_value % 4 != 0:
        explanation = "It is not divisible by 4."
    elif year_value % 100 == 0 and year_value % 400 != 0:
        explanation = "It is divisible by 100 but not divisible by 400."
    else:
        explanation = "It does not meet leap year conditions."

print("\nLeap Year Result")
print("Year:", year_value)
print("Status:", status_text)
print("Reason:", explanation)