
# Q2: OTP Verification Using Loops
# Register Number: 1912260087

CORRECT_OTP = "123456"


# Implementation 1: Using while loop
def verify_using_while(entries):

    attempts = 0
    index = 0

    while attempts < 3 and index < len(entries):

        otp = entries[index]
        index += 1

        if otp == "":
            print("Blank entry - attempt not counted")
            pass
            continue

        attempts += 1
        print("Attempt:", attempts)

        if otp == CORRECT_OTP:
            print("OTP verified successfully!")
            break

        print("Incorrect OTP")

    else:
        if attempts == 3:
            print("Account locked for 30 minutes")
        else:
            print("No more entries available")

    print("Total attempts:", attempts)


# Implementation 2: Using for loop

def verify_using_for(entries):

    attempts = 0
    index = 0

    for _ in range(3):

        while index < len(entries) and entries[index] == "":
            print("Blank entry - attempt not counted")
            pass
            index += 1

        if index >= len(entries):
            print("No more entries available")
            break

        otp = entries[index]
        index += 1
        attempts += 1

        print("Attempt:", attempts)

        if otp == CORRECT_OTP:
            print("OTP verified successfully!")
            break

        print("Incorrect OTP")

    else:
        print("Account locked for 30 minutes")

    print("Total attempts:", attempts)


# Test cases
print("===== WHILE LOOP =====")
verify_using_while(["", "111111", "222222", "333333"])

print("\n===== FOR LOOP =====")
verify_using_for(["", "111111", "222222", "333333"])

print("\n===== SUCCESSFUL VERIFICATION =====")
verify_using_while(["111111", "123456"])