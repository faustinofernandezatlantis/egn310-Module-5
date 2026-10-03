"""
EGN 310 Data Structures
Module 5: Recursion Set (starter file)
"""

# ---------------------------------------------------------------
# Function 1: factorial
# factorial(5) -> 5 * 4 * 3 * 2 * 1 -> 120
# factorial(0) -> 1
# ---------------------------------------------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# ---------------------------------------------------------------
# Function 2: sum_digits
# Add up the digits of a non-negative whole number.
# sum_digits(472) -> 4 + 7 + 2 -> 13
# ---------------------------------------------------------------
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)


# ---------------------------------------------------------------
# Function 3: reverse_string
# reverse_string("cat") -> "tac"
# reverse_string("") -> ""
# ---------------------------------------------------------------
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]


# ---------------------------------------------------------------
# Function 4: power (CONVERT FROM ITERATIVE)
# power(2, 5) -> 32
# power(7, 0) -> 1
# ---------------------------------------------------------------
def power_iterative(base, exp):
    result = 1
    for _ in range(exp):
        result = result * base
    return result


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)