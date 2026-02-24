import random

bestScore = None 

def playGame():
    global bestScore

    secret = random.randint(1, 100)
    tries_left = 7
    tries_used = 0

    print("\nI have selected a number between 1 and 100.")
    # print(f"(Debug: {secret})")  #testing

    while tries_left > 0:

        try:
            guess_input = input(f"\nEnter your guess ({tries_left} attempts left): ")
            guess_num = int(guess_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        tries_used += 1
        tries_left -= 1

        if guess_num == secret:

            print(f"\n🎉 Correct! You guessed it in {tries_used} attempts.")

            if bestScore is None or tries_used < bestScore:
                bestScore = tries_used
                print("🏆 New BEST score!")

            return  # exit current game

        elif guess_num > secret:
            print("Too HIGH!")
        else:
            print("Too LOW!")

        # Close hint
        difference = abs(guess_num - secret)
        if difference <= 5:
            print("🔥 Very close!")

    print(f"\n❌ Game Over! The number was {secret}")

while True:

    playGame()

    again_input = input("\nPlay again? (yes/no): ")
    again_input = again_input.strip().lower()

    if again_input != "yes":
        print("Thanks for playing!")
        break
