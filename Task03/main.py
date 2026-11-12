
# Q3: Vehicle Registration Number Validator
# Register Number: 1912260087

def normalise(text):
    # TODO 1: Remove spaces and hyphens, convert to uppercase
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.upper()
    return text


def is_valid(reg):
    # TODO 2: Validate registration number

    if len(reg) != 9 and len(reg) != 10:
        return False

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    if not state.isalpha():
        return False

    if not district.isdigit():
        return False

    if not series.isalpha():
        return False

    if not number.isdigit():
        return False

    return True


def format_registration(reg):
    # Format as TN 09 AB 1234
    return reg[0:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


# Six test inputs with predictions
test_numbers = [
    "tn 09 ab 1234",
    "TN-09-AB-1234",
    "Tn09Ab1234",
    "KA 05 C 9876",
    "TN 9 AB 1234",
    "1234 AB 09 TN"
]

print("VEHICLE REGISTRATION VALIDATOR")
print("-" * 55)

print("\nPredictions before execution:")
for number in test_numbers:
    print(number, ":", "Valid" if (
        len(number.replace(" ", "").replace("-", "")) in (9, 10)
        and (
            lambda r: r[0:2].isalpha()
            and r[2:4].isdigit()
            and r[4:-4].isalpha()
            and r[-4:].isdigit()
        )(normalise(number))
    ) else "Invalid")

print("\nActual results:")
for number in test_numbers:
    result = normalise(number)

    if is_valid(result):
        print(number, "->", format_registration(result), "-> VALID")
    else:
        print(number, "->", result, "-> INVALID")