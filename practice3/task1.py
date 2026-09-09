print("Diana Melnyk, I-23")

name = input("Enter your full name (Latin letters): ").strip()
age = int(input("Enter your age (integer): "))

if not name:
    print("The name was not entered")
    name = "Anonymous"

if age < 0:
    category = "invalid value"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"

print(f"Hello, {name}! Your category is {category}.")