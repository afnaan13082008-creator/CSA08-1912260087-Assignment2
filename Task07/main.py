
# Q7: Diagnose, Redesign and Validate
# Register Number: 1912260087
# Selected program: Q4 - String Building

import time

SIZES = [1000, 10000, 50000]
REPETITIONS = 3


# Generate identical input for both methods
def generate_items(n):
    return [f"Item{i}:Rs{i % 50}" for i in range(n)]


# ORIGINAL IMPLEMENTATION
def original_build(parts):
    text = ""

    for p in parts:
        text = text + p + ","

    return text


# REDESIGNED IMPLEMENTATION
def redesigned_build(parts):
    chunks = []

    for p in parts:
        chunks.extend((p, ","))

    return "".join(chunks)


# Measure execution time and average
def benchmark(function, parts):

    times = []
    result = ""

    for _ in range(REPETITIONS):

        start = time.perf_counter()
        result = function(parts)
        end = time.perf_counter()

        times.append(end - start)

    average = sum(times) / len(times)

    return result, average, times


# MAIN PROGRAM
print("Q7: DIAGNOSE, REDESIGN AND VALIDATE")
print("=" * 65)

for size in SIZES:

    print(f"\nINPUT SIZE: {size} LINES")
    print("-" * 65)

    items = generate_items(size)

    # Original method
    original_result, original_avg, original_times = benchmark(
        original_build, items
    )

    # Redesigned method
    new_result, new_avg, new_times = benchmark(
        redesigned_build, items
    )

    # Correctness validation
    print("Same output:", original_result == new_result)
    print("Output characters:", len(original_result))

    # Operation counts
    print("\nORIGINAL METHOD:")
    print("String concatenations:", size * 2)
    print("Repeated full-string rebuilding: Yes")

    print("\nREDESIGNED METHOD:")
    print("List extend operations:", size)
    print("Final join operations: 1")
    print("Repeated full-string rebuilding: No")

    # Timing evidence
    print("\nORIGINAL RUN TIMES:", original_times)
    print(f"Original average: {original_avg:.6f} seconds")

    print("\nREDESIGNED RUN TIMES:", new_times)
    print(f"Redesigned average: {new_avg:.6f} seconds")

    # Calculate improvement
    if new_avg > 0:
        speedup = original_avg / new_avg

        print(f"\nSpeedup: {speedup:.2f} times faster")

print("\nALL VALIDATION TESTS COMPLETED")