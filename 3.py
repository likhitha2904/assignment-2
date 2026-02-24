
sentence_input = input("Enter a sentence: ")
sentence_input = sentence_input.strip()  # removing accidental leading/trailing spaces basically

# Basic validation
if sentence_input == "":
    print("Invalid input! Please enter something next time.")
    quit()  # using quit(), its a habit

originalText = sentence_input  

# counting characters
char_count_with_spaces = len(originalText)

temp_no_spaces = originalText.replace(" ", "")
char_count_without_spaces = len(temp_no_spaces)

# Word details
words = originalText.split()
num_of_words = len(words)

# Case variations
upper_version = originalText.upper()
lower_version = originalText.lower()
titleVersion = originalText.title()  # inconsistent naming (intentionally human)

# First and last words
firstWord = words[0]
last_word = words[-1]

# Reverse manually (not the most efficient way, but readable)
reversed_text = ""
for ch in originalText:
    reversed_text = ch + reversed_text

print("\nResults")
print("Original:", originalText)
print("Characters (with spaces):", char_count_with_spaces)
print("Characters (without spaces):", char_count_without_spaces)
print("Words:", num_of_words)

print("UPPERCASE:", upper_version)
print("lowercase:", lower_version)
print("Title Case:", titleVersion)

print("First word:", firstWord)
print("Last word:", last_word)

print("Reversed:", reversed_text)

# Might extend this later (maybe vowel/consonant counting?)