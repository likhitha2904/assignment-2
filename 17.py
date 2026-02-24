user_input = input("Enter word/number: ")

# Normalizing
processed_text = user_input.lower()

# Reversing manually
reversed_version = ""

for ch in processed_text:
    reversed_version = ch + reversed_version   # building reversed string

print("\nOriginal:", user_input)
print("Normalized:", processed_text)
print("Reversed:", reversed_version)

#comparison
if processed_text == reversed_version:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")
