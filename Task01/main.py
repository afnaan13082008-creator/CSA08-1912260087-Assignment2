
# Q1: State Electricity Subsidy Eligibility
# Register Number: 1912260087

households = [
    ("H1", 100, False, False),
    ("H2", 101, True, False),
    ("H3", 101, False, False),
    ("H4", 200, True, False),
    ("H5", 200, False, True),
    ("H6", 201, False, True),
    ("H7", 201, True, False),
    ("H8", 80, True, True)
]

# Implementation 1: Separate if statements
def separate_if(units, ration, senior):
    results = []

    if units <= 100:
        results.append("Full Subsidy")

    if 101 <= units <= 200 and ration:
        results.append("Partial Subsidy")

    if units > 200 and senior:
        results.append("Special Subsidy")

    if not results:
        results.append("No Subsidy")

    return results


# Implementation 2: if-elif-else
def if_elif_else(units, ration, senior):

    if units <= 100:
        return ["Full Subsidy"]

    elif 101 <= units <= 200 and ration:
        return ["Partial Subsidy"]

    elif units > 200 and senior:
        return ["Special Subsidy"]

    else:
        return ["No Subsidy"]


# Display predictions and compare both methods
print("ELECTRICITY SUBSIDY ELIGIBILITY")
print("-" * 65)

print("\nPredicted decisions before execution:")
for name, units, ration, senior in households:
    if units <= 100:
        prediction = "Full Subsidy"
    elif 101 <= units <= 200 and ration:
        prediction = "Partial Subsidy"
    elif units > 200 and senior:
        prediction = "Special Subsidy"
    else:
        prediction = "No Subsidy"

    print(name, ":", prediction)

print("\nComparison of both implementations:")
for name, units, ration, senior in households:

    result1 = separate_if(units, ration, senior)
    result2 = if_elif_else(units, ration, senior)

    print(f"{name} ({units} units):")
    print("Separate if :", result1)
    print("If-elif-else:", result2)
    print("Match:", result1 == result2)
    print()

# Demonstrate the overlapping-condition problem
print("Demonstrating overlapping conditions:")

units = 100
ration = True
results = []

if units <= 100:
    results.append("Full Subsidy")

if units <= 200 and ration:
    results.append("Partial Subsidy")

print("Incorrect separate-if result:", results)