
---

### Hand Trace: `reverse_string("cat")`

**1. Call Stack Growth (Expansion / Pushing onto stack):**

* `reverse_string("cat")` $\rightarrow$ calls `reverse_string("at") + "c"`
* `reverse_string("at")` $\rightarrow$ calls `reverse_string("t") + "a"`
* `reverse_string("t")` $\rightarrow$ calls `reverse_string("") + "t"`
* `reverse_string("")` $\rightarrow$ Base case reached (`len(s) == 0`), returns `""`

**2. Unwinding Stack (Popping from stack and evaluating):**

* `reverse_string("t")` returns `"" + "t"` = `"t"`
* `reverse_string("at")` returns `"t" + "a"` = `"ta"`
* `reverse_string("cat")` returns `"ta" + "c"` = `"tac"`

**Final Output:** `"tac"`

---

### Alternative Hand Trace: `factorial(4)`

**1. Call Stack Growth (Expansion / Pushing onto stack):**

* `factorial(4)` $\rightarrow$ calls `4 * factorial(3)`
* `factorial(3)` $\rightarrow$ calls `3 * factorial(2)`
* `factorial(2)` $\rightarrow$ calls `2 * factorial(1)`
* `factorial(1)` $\rightarrow$ calls `1 * factorial(0)`
* `factorial(0)` $\rightarrow$ Base case reached (`n == 0`), returns `1`

**2. Unwinding Stack (Popping from stack and evaluating):**

* `factorial(1)` returns `1 * 1` = `1`
* `factorial(2)` returns `2 * 1` = `2`
* `factorial(3)` returns `3 * 2` = `6`
* `factorial(4)` returns `4 * 6` = `24`

**Final Output:** `24`