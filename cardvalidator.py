def get_card_type(card_number):
    """Detects the card type and returns the type + expected length."""
    if card_number.startswith("4"):
        return "Visa", 13, 16, 19
    elif card_number.startswith(("51", "52", "53", "54", "55")) or \
         (len(card_number) >= 4 and 2221 <= int(card_number[:4]) <= 2720):
        return "Mastercard", 16, 16, 16
    elif card_number.startswith(("34", "37")):
        return "American Express", 15, 15, 15
    elif card_number.startswith(("6011", "65")):
        return "Discover", 16, 16, 19
    elif card_number.startswith(("300", "301", "302", "303", "304", "305", "36", "38")):
        return "Diners Club", 14, 14, 14
    elif card_number.startswith("35"):
        return "JCB", 16, 16, 19
    else:
        return "Unknown", 13, 19, 19


def verify_card_number(card_number):
    """Validates a card number using the Luhn Algorithm."""
    card_number = card_number.replace(" ", "").replace("-", "")

    if not card_number.isdigit():
        return False

    card_number_reversed = card_number[::-1]
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for digit in card_number_reversed[::2]:
        sum_of_odd_digits += int(digit)

    for digit in card_number_reversed[1::2]:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0


def main():
    print("=== Card Number Validator ===")
    print("Type 'quit' to exit.\n")

    while True:
        card_number = input("Enter card number: ").strip()

        if card_number.lower() == "quit":
            print("Goodbye!")
            break

        cleaned_number = card_number.replace(" ", "").replace("-", "")

        if not cleaned_number.isdigit():
            print("Invalid input. Please enter numbers only.\n")
            continue

        is_valid = verify_card_number(cleaned_number)
        card_type, min_len, normal_len, max_len = get_card_type(cleaned_number)
        length = len(cleaned_number)

        print(f"Card Type: {card_type}")
        print(f"Length: {length} (Expected: {min_len}-{max_len})")

        if is_valid:
            print("Status: VALID!\n")
        else:
            print("Status: INVALID!\n")


if __name__ == "__main__":
    main()