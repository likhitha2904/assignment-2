
balance = 10000.0   # using float
min_required_balance = 500

print(" ATM SIMULATOR ")

running = True   # using flag instead of while True (easier for me)

while running:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice_input = input("Enter choice: ")
        option = int(choice_input)
    except ValueError:
        print("Invalid choice! Please enter a number between 1-4.")
        continue

    #checking balance
    if option == 1:
        print(f"Current Balance: Rs.{balance:.2f}")

    #deposit
    elif option == 2:
        try:
            deposit_input = input("Enter amount to deposit: Rs.")
            deposit_amt = float(deposit_input)

            if deposit_amt <= 0:
                raise ValueError("Deposit amount must be positive.")

            # updating balance
            balance += deposit_amt   
            print("Deposit successful!")
            print(f"Updated Balance: Rs.{balance:.2f}")

        except ValueError as err:
            print("Invalid input:", err)

    #withdraw
    elif option == 3:
        try:
            withdraw_input = input("Enter amount to withdraw: Rs.")
            withdraw_amt = float(withdraw_input)

            if withdraw_amt <= 0:
                raise ValueError("Withdrawal amount must be positive.")

            # Checking sufficient balance
            if withdraw_amt > balance:
                print("Insufficient balance!")

            elif (balance - withdraw_amt) < min_required_balance:
                print("Transaction denied! Minimum ₹500 balance must remain.")

            else:
                balance -= withdraw_amt  
                print("Withdrawal successful!")
                print(f"New Balance: Rs.{balance:.2f}")

        except ValueError as err:
            print("Invalid input:", err)
    #exit
    elif option == 4:
        print("Thank you for using the ATM. Goodbye!")
        running = False 
    #invalid
    else:
        print("Invalid choice! Please select between 1-4.")


