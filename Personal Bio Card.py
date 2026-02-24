student_name= input("enter your full name").strip()  #used strip() to make the alignment proper, just in case.

#used try-except to handle negative age values
try:
    student_age=int(input("enter age"))
    if student_age <=0:
        raise ValueError("how can age be negative?")
except ValueError:
    print("invalid age entered, so it will be set as 'not provided'")
    student_age= "not provided"

student_course= input("enter your course name").strip()
student_college= input("enter your college name").strip()
student_mail= input("enter your email address").strip()

card_width=40
print("\n" + "╔" + "═" * card_width + "╗")

# Title centered
print("║" + "STUDENT BIO CARD".center(card_width) + "║")

# Separator
print("╠" + "═" * card_width + "╣")

# Displaying formatted information
print("║ " + f"Name    : {student_name}".ljust(card_width - 1) + "║")
print("║ " + f"Age     : {student_age} years".ljust(card_width - 1) + "║")
print("║ " + f"Course  : {student_course}".ljust(card_width - 1) + "║")
print("║ " + f"College : {student_college}".ljust(card_width - 1) + "║")
print("║ " + f"Email   : {student_mail}".ljust(card_width - 1) + "║")

# Bottom border
print("╚" + "═" * card_width + "╝")