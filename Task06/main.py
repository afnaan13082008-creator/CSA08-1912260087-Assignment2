
# Q6: Recursion and Memoisation
# Register Number: 1912260087

from functools import lru_cache
import sys

# Count function calls
calls = 0


# PART 1: Plain recursive solution
def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# PART 2: Memoised recursive solution
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# PART 3: Iterative solution
def ways_loop(n):

    if n <= 1:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# PART 4: Manual correctness verification
print("===== CORRECTNESS CHECK =====")

for n in range(1, 7):
    calls = 0
    result = ways_naive(n)

    print(f"n = {n}, ways = {result}")


# PART 5: Call tree for n = 5
print("\n===== CALL TREE FOR n = 5 =====")

print("""
ways(5)
├── ways(4)
│   ├── ways(3)
│   │   ├── ways(2)
│   │   └── ways(1)
│   └── ways(2)
└── ways(3)
    ├── ways(2)
    └── ways(1)

Repeated calculations: ways(3), ways(2), etc.
""")


# PART 6: Compare function calls
print("===== GROWTH INVESTIGATION =====")

for n in [10, 20, 25, 30]:

    calls = 0
    naive_result = ways_naive(n)
    naive_calls = calls

    calls = 0
    ways_memo.cache_clear()
    memo_result = ways_memo(n)
    memo_calls = calls

    print(f"\nn = {n}")
    print("Naive result:", naive_result)
    print("Naive calls:", naive_calls)
    print("Memoised result:", memo_result)
    print("Memoised calls:", memo_calls)


# PART 7: Test n = 1000
print("\n===== DEPLOYMENT DECISION =====")

calls = 0
ways_memo.cache_clear()

print("Python recursion limit:", sys.getrecursionlimit())

try:
    result = ways_memo(1000)
    print("Memoised result for 1000:", result)

except RecursionError:
    print("RecursionError occurred at n = 1000")
    print("Memoisation removes repeated work,")
    print("but does not remove recursion depth.")


# PART 8: Iterative solution for n = 1000
result = ways_loop(1000)

print("\nIterative solution for n = 1000:")
print("Number of digits:", len(str(result)))
print("Result calculated successfully!")

print("\nProgram completed.")