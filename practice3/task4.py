print("Diana Melnyk, I-23")

score = int(input("Enter your score (0-100): "))
missed = int(input("Enter the number of missed classes (integer): "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    if missed > 16 * 0.3:
        print("Warning: you are not admitted because of too many missed classes")

    if score >= 60 and missed <= 16 * 0.3:
        status = "passed"
    else:
        status = "failed"

    print(f"Score: {score}, Grade: {grade}, Result: {status}")