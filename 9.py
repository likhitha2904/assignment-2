try:
    age_input = input("Enter age: ")
    age = int(age_input)

    day_input = input("Enter day of week: ")
    day = day_input.strip().lower()

    ticket_count = int(input("Enter number of tickets: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if ticket_count <= 0:
        raise ValueError("Number of tickets must be at least 1.")

except ValueError as err:
    print("Invalid input:", err)
    quit()   

# Setting defaults first, just in case)
ticket_price = 0
ticket_category = "Unknown"

if age < 3:
    ticket_price = 0
    ticket_category = "Free"

elif age >= 3 and age <= 12:
    ticket_price = 150
    ticket_category = "Child"

elif age >= 13 and age <= 59:
    ticket_price = 300
    ticket_category = "Adult"

else:
    ticket_price = 200
    ticket_category = "Senior"


# I’m including Friday as weekend here, because who doesn't go out on a friday night?
weekend_list = ["friday", "saturday", "sunday"]

discount_percent = 0  # default no discount

if day in weekend_list:
    discount_percent = 20

# Calculate discount
discount_value = (ticket_price * discount_percent) / 100
final_price_per_ticket = ticket_price - discount_value

# Small redundancy for readability
tickets = ticket_count
total_cost = final_price_per_ticket * tickets

print("\n TICKET BILL")

print("Category:", ticket_category)
print(f"Base Price per Ticket: ₹{ticket_price:.2f}")
print(f"Discount Applied: {discount_percent}%")
print(f"Price After Discount (per ticket): Rs.{final_price_per_ticket:.2f}")

print("-" * 30)

print(f"Number of Tickets: {tickets}")
print(f"Total Amount: Rs.{total_cost:.2f}")
