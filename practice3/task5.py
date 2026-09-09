print("Diana Melnyk, I-23")

day = int(input("Enter the day of birth (integer): "))
month = int(input("Enter the month of birth (integer): "))
year = int(input("Enter the year of birth (integer): "))

if year <= 0:
    print(f"Date is invalid: year {year} must be positive")
elif month < 1 or month > 12:
    print(f"Date is invalid: month {month} must be between 1 and 12")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_day = 29
        else:
            max_day = 28
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        max_day = 31

    if day < 1 or day > max_day:
        print(f"Date is invalid: month {month} has only {max_day} days")
    else:
        print(f"Date is valid: {day:02d}.{month:02d}.{year}")