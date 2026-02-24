try:
    choice_input = input("Enter pattern choice (1-4): ")
    pattern_option = int(choice_input)

    height_input = input("Enter height: ")
    height = int(height_input)

    if height <= 0:
        raise ValueError("Height must be positive.")

except ValueError as err:
    print("Invalid input:", err)
    quit()

print("\nGenerated Pattern:\n")

#pattern1
if pattern_option == 1:
    for r in range(1, height + 1):
        for num in range(1, r + 1):
            print(num, end=" ")
        print()   # move to next line

#pattern2
elif pattern_option == 2:
    for r in range(1, height + 1):
        for _ in range(r):
            print(r, end=" ")
        print()

#pattern3
elif pattern_option == 3:
    # Reverse decreasing pattern
    for r in range(height, 0, -1):
        for num in range(r, 0, -1):
            print(num, end=" ")
        print()

#pattern4
elif pattern_option == 4:
    # Pyramid-style number pattern
    for r in range(1, height + 1):
        # Increasing part
        for num in range(1, r + 1):
            print(num, end="")
        # Decreasing part
        for num in range(r - 1, 0, -1):
            print(num, end="")
        print()   # newline

# Invalid Choice
else:
    print("Invalid pattern choice! Please select between 1-4.")
