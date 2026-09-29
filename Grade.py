def get_grade(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


try:
    score = int(input("Enter your score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter 0 to 100.")
    else:
        grade = get_grade(score)
        print("Your score is:", score)
        print("Your grade is:", grade)

except ValueError:
    print("Please enter a valid number 0 to 100.")