```markdown
# Bisection Method for Square Root Calculation

This project implements the **Bisection Method** to approximate the square root of a number without importing any external modules. The bisection method iteratively narrows down an interval where the square root lies until the approximation is within a specified tolerance.

---

## Objective

Create a function `square_root_bisection` that accepts a number and finds its square root using the bisection method, adhering to the following specifications:

- Raise a `ValueError` if the number is negative.
- Handle special cases for 0 and 1.
- For other positive numbers, iteratively approximate the square root.
- Print informative messages about the process and results.
- Return the approximate square root or `None` if convergence isn't achieved within the maximum iterations.

---

## User Stories & Implementation Details

### Function Signature

```python
def square_root_bisection(num, tolerance=1e-7, max_iter=100):
``

- `num`: The target number to find the square root of.
- `tolerance` (default: `1e-7`): The acceptable error margin for the approximation.
- `max_iter` (default: `100`): The maximum number of iterations to perform.

---

### Behavior & Requirements

1. **Negative Input:**
    - If `num < 0`, raise a `ValueError` with the message:
      `"Square root of negative number is not defined in real numbers"`

2. **Special Cases:**
    - If `num` is `0`, print:
      `"The square root of 0 is 0"` and return `0`.
    - If `num` is `1`, print:
      `"The square root of 1 is 1"` and return `1`.

3. **Approximation for Positive Numbers > 1:**
    - Set initial bounds:
        - `low = 0`
        - `high = max(1, num)` (to handle numbers less than 1)
    - Use the bisection method:
        - Calculate `guess = (high + low) / 2`
        - Compute `squared_guess = guess * guess`
        - If `(high - low) <= tolerance`, consider the approximation converged:
            - Print: `"The square root of [num] is approximately [guess]"`
            - Return `guess`
        - Otherwise, update bounds:
            - If `squared_guess > num`, set `high = guess`
            - Else, set `low = guess`
    - Repeat until convergence or max iterations.

4. **Failure to Converge:**
    - If the loop completes without satisfying the tolerance condition, print:
      `"Failed to converge within [max_iter] iterations"` and return `None`.

---

## Example Usage

```python
# Find the square root of 0.001
result = square_root_bisection(0.001)
# Output:
# The square root of 0.001 is approximately 0.031622776...
``

---

## Notes

- The function does not import any modules.
- It is designed to be robust and handle edge cases gracefully.
- The printed messages provide insight into the approximation process and results.

---

## Testing

Ensure your implementation passes all the provided test cases, including:

- Handling negative inputs.
- Correctly computing square roots of perfect squares.
- Approximating non-perfect squares within specified tolerances.
- Handling maximum iteration limits appropriately.
