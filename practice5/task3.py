def get_initials(name: str, surname: str) -> str:
    """Return initials of a name and surname."""
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    return text.lower().count(letter.lower())


def count_vowels(text: str) -> int:
    """Return the number of vowels in text."""
    vowels = "aeiouy"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


def reverse_text(text: str) -> str:
    """Return text in reverse order without slicing."""
    result = ""

    for char in text:
        result = char + result

    return result


def main():
    name = "Diana"
    surname = "Melnyk"

    print("Diana Melnyk, I-23")
    print("Initials:", get_initials(name, surname))

    c = len(surname)
    vowels = count_vowels(surname)
    consonants = c - vowels

    print("Letters in surname:", c)
    print("Vowels:", vowels)
    print("Consonants:", consonants)

    for vowel in "aeiou":
        print(
            f"{vowel}:",
            count_letters(surname, letter=vowel)
        )

    print("Default letter 'a':", count_letters(surname))
    print("Reversed surname:", reverse_text(surname))

    print("Docstring:", count_letters.__doc__)
    print("Annotations:", count_letters.__annotations__)


main()