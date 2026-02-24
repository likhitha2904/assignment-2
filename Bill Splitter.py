try:
    raw_bill = input("Enter total bill amount: ₹ ")
    totalBill = float(raw_bill)   # converting separately 

    people_count = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    # Basic validations
    if totalBill < 0:
        raise ValueError("Bill amount cannot be negative.")

    if people_count <= 0:
        raise ValueError("Number of people must be at least 1.")

    if tax_percent < 0 or tip_percent < 0:
        raise ValueError("Tax/Tip percentages cannot be negative.")

except ValueError as err:
    print("Invalid input:", err)
    quit()   


subtotal_amount = totalBill  

# Tax calculation
tax_value = (subtotal_amount * tax_percent) / 100
after_tax_total = subtotal_amount + tax_value

# Tip calculation (applied after tax)
tip_value = (after_tax_total * tip_percent) / 100

# Final total
grand_total = after_tax_total + tip_value

# Splitting
# Could technically check again for division by zero, but we already validated people_count earlier.
per_head_amount = grand_total / people_count

print("\n=== BILL BREAKDOWN ===")

print(f"Subtotal:        ₹{subtotal_amount:.2f}")
print(f"Tax ({tax_percent}%):      ₹{tax_value:.2f}")
print(f"After tax:       ₹{after_tax_total:.2f}")
print(f"Tip ({tip_percent}%):      ₹{tip_value:.2f}")

print("-" * 30)  # separator line

print(f"Total:           ₹{grand_total:.2f}")
print(f"Per person:      ₹{per_head_amount:.2f}")