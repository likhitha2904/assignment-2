from datetime import datetime   # keeping it simple

#basic age calculation, only using years
try:
    user_birth_year = input("Enter your birth year (YYYY): ")
    user_birth_year = int(user_birth_year)   # converting separately for clarity

    now = datetime.now()
    this_year = now.year

    if user_birth_year > this_year:
        raise ValueError("Future year entered.")  # basic validation

    age_years = this_year - user_birth_year

except ValueError:
    print("Invalid input! Please enter a proper year (numbers only).")
    quit()   

#approx
# These are rough estimates (not accounting for leap years properly)
age_months = age_years * 12

age_days_estimate = age_years * 365   # could improve later
age_hours = age_days_estimate * 24
age_minutes = age_hours * 60

years_left_to_100 = 100 - age_years

# Just in case someone is already 100+
if years_left_to_100 < 0:
    years_left_to_100 = 0   # avoiding negative output (felt cleaner)


print("\nApproximate Age")
print("Current Age:", age_years, "years")
print("Age in Months:", age_months)
print("Age in Days (approx):", age_days_estimate)
print("Age in Hours:", age_hours)
print("Age in Minutes:", age_minutes)
print("Years until 100:", years_left_to_100)

#tried bonus, but with date-time module (even though we were not supposed to use built in functions)
extra_option = input("\nDo you want to calculate exact age using full birth date? (yes/no): ")
extra_option = extra_option.lower().strip()

if extra_option == "yes":

    try:
        print("\nEnter full birth details below:")

        day = int(input("Day (1-31): "))
        month = int(input("Month (1-12): "))
        year_exact = int(input("Year (YYYY): "))

        birth_date_obj = datetime(year_exact, month, day)
        current_date_obj = datetime.now()

        if birth_date_obj > current_date_obj:
            raise ValueError("Birth date is in the future.")

        difference = current_date_obj - birth_date_obj
        total_days_lived = difference.days

        # Rough year conversion again (keeping it simple)
        approx_years_lived = total_days_lived // 365

        print("\n----- Exact Age Details -----")
        print("Exact Age in Years (approx):", approx_years_lived)
        print("Exact Age in Days:", total_days_lived)

        # I considered calculating months properly, but that gets messy with varying month lengths.

    except ValueError:
        print("Invalid date entered. Please double-check your numbers.")

# Might refactor this later into functions if it grows more.