def print_card():
    """Print my personal card without parameters."""
    print("Name: Diana Melnyk")
    print("Group: I-23")
    print("Birth year: 2008")


def print_card_args(name, surname, group="I-23", year=2008):
    """Print a personal card using parameters."""
    print(f"{name} {surname}, {group}, {year}")


def main():
    print("Diana Melnyk, I-23")

    print("--- no parameters, call 1 ---")
    print_card()

    print("--- no parameters, call 2 ---")
    print_card()

    print("--- no parameters, call 3 ---")
    print_card()

    print("--- positional arguments ---")
    print_card_args("Diana", "Melnyk", "I-23", 2008)

    print("--- keyword arguments ---")
    print_card_args(year=2008, group="I-23", surname="Melnyk", name="Diana")

    print("--- mixed arguments ---")
    print_card_args("Diana", "Melnyk", group="I-23", year=2008)

    print("--- default group ---")
    print_card_args("Diana", "Melnyk", year=2008)


main()