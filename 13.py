try:
    count_input = input("How many numbers? ")
    total_count = int(count_input)

    if total_count <= 0:
        raise ValueError("Count must be positive.")

except ValueError as err:
    print("Invalid input:", err)
    quit()  


#Initialization
sum_total = 0   # accumulator for sum
max_value = None
min_value = None

for i in range(1, total_count + 1):

    try:
        num_input = input(f"Enter number {i}: ")
        current_val = float(num_input)
    except ValueError:
        print("Invalid number entered.")
        quit()

    # Adding to total
    sum_total += current_val 

    # Updating maximum
    if max_value is None:
        max_value = current_val
    elif current_val > max_value:
        max_value = current_val

    # Updating minimum
    if min_value is None:
        min_value = current_val
    elif current_val < min_value:
        min_value = current_val

average = sum_total / total_count

print("\n RESULTS ")
print("Sum:", sum_total)
print("Average:", average)
print("Maximum:", max_value)
print("Minimum:", min_value)
