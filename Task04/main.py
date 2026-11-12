
# Q4: Building Long Text - + vs join()
# Register Number: 1912260087

import time

# Three different test sizes
SIZES = [1000, 10000, 200000]

# Generate SMS bill statement lines
def generate_items(n):
    return [f"Item{i}:Rs{i % 50}" for i in range(n)]


# Method 1: Repeated + inside a loop
def build_plus(parts):
    text = ""

    for p in parts:
        text = text + p + ","

    return text


# Method 2: List followed by join()
def build_join(parts):
    return ",".join(parts) + ","


# Method 3: F-string for each line, followed by join()
def build_fstring(parts):
    lines = [f"{p}," for p in parts]
    return "".join(lines)


# Measure execution time

def measure(function, parts, repetitions=None):

    if repetitions is None:
        repetitions = 3 if len(parts) <= 10000 else 1

    times = []

    for _ in range(repetitions):
        start = time.perf_counter()
        result = function(parts)
        end = time.perf_counter()

        times.append(end - start)

    average = sum(times) / len(times)

    return result, average

# Main benchmark
print("SMS BILL STATEMENT PERFORMANCE")
print("=" * 65)

for size in SIZES:

    print(f"\nNumber of lines: {size}")

    items = generate_items(size)

    plus_result, plus_time = measure(build_plus, items)
    join_result, join_time = measure(build_join, items)
    fstring_result, fstring_time = measure(build_fstring, items)

    # Verify all methods produce the same output
    print("Same output:", plus_result == join_result == fstring_result)
    print("Total characters:", len(plus_result))

    print(f"Repeated + average : {plus_time:.6f} seconds")
    print(f"join() average     : {join_time:.6f} seconds")
    print(f"f-string average   : {fstring_time:.6f} seconds")

    # Predict the fastest method
    fastest = min(
        [
            (plus_time, "Repeated +"),
            (join_time, "join()"),
            (fstring_time, "f-string + join")
        ]
    )

    print("Fastest method:", fastest[1])

print("\nBenchmark completed.")