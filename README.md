# Module 5: Recursion Set

This repository contains the solution for the **EGN 310 Data Structures - Module 5 Recursion Assignment**.

## Overview

The goal of this assignment is to implement recursive algorithms without using iterative constructs (`for` or `while` loops). Each function includes a defined **base case** and a **recursive case**.

### Functions Implemented

1. **`factorial(n)`**: Calculates $n!$ recursively.
2. **`sum_digits(n)`**: Sums the individual digits of a non-negative integer using `% 10` and `// 10`.
3. **`reverse_string(s)`**: Reverses a string using string slicing.
4. **`power(base, exp)`**: Converted from an iterative loop to a recursive algorithm ($base^{exp}$).

## Requirements & Testing

The tests ensure both correctness and strict compliance with recursion constraints (checking that functions call themselves and contain no loop AST nodes).

### Running Tests

Run tests using `pytest`:
```bash
pytest test_recursion.py -v