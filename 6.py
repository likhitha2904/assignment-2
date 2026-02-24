try: #can use list instead
    s1 = float(input("Enter marks for Subject 1 (0-100): "))
    s2 = float(input("Enter marks for Subject 2 (0-100): "))
    s3 = float(input("Enter marks for Subject 3 (0-100): "))
    s4 = float(input("Enter marks for Subject 4 (0-100): "))
    s5 = float(input("Enter marks for Subject 5 (0-100): "))

    # Manual validation 
    if s1 < 0 or s1 > 100:
        raise ValueError("Subject 1 marks out of range.")
    if s2 < 0 or s2 > 100:
        raise ValueError("Subject 2 marks out of range.")
    if s3 < 0 or s3 > 100:
        raise ValueError("Subject 3 marks out of range.")
    if s4 < 0 or s4 > 100:
        raise ValueError("Subject 4 marks out of range.")
    if s5 < 0 or s5 > 100:
        raise ValueError("Subject 5 marks out of range.")

except ValueError as err:
    print("Invalid input:", err)
    quit()   


# Calculating total 
totalMarks = s1 + s2 + s3 + s4 + s5

maximum_marks = 500  # 5 subjects × 100
percent = (totalMarks / maximum_marks) * 100

# Simple if-elif ladder (easy to read)
if percent >= 90:
    grade_obtained = "A+ (Outstanding)"
elif percent >= 80:
    grade_obtained = "A (Excellent)"
elif percent >= 70:
    grade_obtained = "B (Good)"
elif percent >= 60:
    grade_obtained = "C (Average)"
elif percent >= 50:
    grade_obtained = "D (Pass)"
else:
    grade_obtained = "F (Fail)"


# Writing it explicitly instead of compressing into one long line
all_passed = True

if s1 < 40:
    all_passed = False
if s2 < 40:
    all_passed = False
if s3 < 40:
    all_passed = False
if s4 < 40:
    all_passed = False
if s5 < 40:
    all_passed = False


if all_passed:
    final_result = "Pass"
else:
    final_result = "Fail"


print("\nRESULT")

print("Subject 1:", s1)
print("Subject 2:", s2)
print("Subject 3:", s3)
print("Subject 4:", s4)
print("Subject 5:", s5)

print("\nTotal Marks:", totalMarks, "/", maximum_marks)
print(f"Percentage: {percent:.2f}%")
print("Grade:", grade_obtained)
print("Result:", final_result)
