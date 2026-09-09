name = "Diana"
surname = "Melnyk"

print("Diana Melnyk, I-23")

text = name + surname

vowels = 0
consonants = 0

for letter in text:
    if letter.lower() in "aeiouy":
        vowels += 1
    else:
        consonants += 1

print(f"Vowels: {vowels}, consonants: {consonants}")
print(f"Total letters: {len(text)}")
print(f"Check: {vowels + consonants == len(text)}")