#counting functions
def countWords(text):
    words = text.split()   #splitting by whitespace
    return len(words)

def countVowels(text):
    vowel_count = 0
    for ch in text.lower():
        if ch in "aeiou":
            vowel_count += 1
    return vowel_count

def countConsonants(text):
    consonant_count = 0
    for ch in text.lower():
        if ch.isalpha() and ch not in "aeiou":
            consonant_count += 1
    return consonant_count

def reverseText(text):
    reversed_version = ""
    for ch in text:
        reversed_version = ch + reversed_version   # building manually
    return reversed_version


def checkPalindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    reversed_cleaned = cleaned_text[::-1]
    return cleaned_text == reversed_cleaned


def removeVowels(text):
    result = ""
    for ch in text:
        if ch.lower() not in "aeiou":
            result += ch
    return result

#woed analysis
def wordFrequency(text):
    words = text.lower().split()
    frequency_dict = {}

    for w in words:
        if w in frequency_dict:
            frequency_dict[w] += 1
        else:
            frequency_dict[w] = 1
    return frequency_dict

def longestWord(text):
    words = text.split()
    if not words:   # handling empty input edge case
        return "", 0
    longest_word_found = words[0]

    for w in words:
        if len(w) > len(longest_word_found):
            longest_word_found = w
    return longest_word_found, len(longest_word_found)


def analyzeText(text):

    print("\nTEXT ANALYSIS")

    print("Words:", countWords(text))
    print("Vowels:", countVowels(text))
    print("Consonants:", countConsonants(text))

    reversed_output = reverseText(text)
    print("Reversed:", reversed_output)

    if checkPalindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", removeVowels(text))

    longest, length = longestWord(text)
    print(f"Longest word: {longest} ({length} letters)")

    freq_data = wordFrequency(text)
    print("Word Frequency:")

    for word in freq_data:
        print(f"{word}: {freq_data[word]}")


user_text_input = input("Enter text: ")
analyzeText(user_text_input)