# INT6181_tutorial_6

Tutorial 6: Test Code in Scale & Fix with Debugger

In this tutorial you will practise writing unit tests with Python's `unittest` framework. For each case, study the given module, write tests that cover the stated rules, and use your tests to check whether the implementation is correct. If your tests reveal incorrect behaviour, fix the code.

The Expected Solution is in `Expected_Solution.png`

---

## Task 1: Password Validator

Write unit tests for `validate_password` in `password_validator.py`.

### Specification

The function must return `True` only when all of the following hold:

1. The input is a string (`str`).
2. The length is between **8 and 20** characters (inclusive).
3. The password contains no whitespace (spaces, tabs, or newlines).
4. The password contains at least:
   - one uppercase letter (`A-Z`)
   - one lowercase letter (`a-z`)
   - one digit (`0-9`)
   - one special character (any non-alphanumeric character)

Otherwise it must return `False`.


---

## Task 2: Triangle Validator

Write unit tests for the `Triangle` in `triangle.py`.

### Specification

Given three side lengths `a`, `b`, and `c`:

1. **Validity** (`is_valid`):
   - All sides must be numbers (`int` or `float`, not `bool`).
   - All sides must be strictly greater than zero.
   - Triangle inequality must hold: \(a + b > c\), \(a + c > b\), \(b + c > a\).
2. **Type** (`get_type`): for a valid triangle, return Equilateral, Isosceles, or Scalene; otherwise return `None`.
3. **Area** (`get_area`): for a valid triangle, compute area with Heron's formula and round to **4** decimal places; otherwise return `None`.


---

## Task 3: Parking Fee Calculator

Write unit tests for `ParkingFeeCalculator` in `parking_fee.py`.

### Specification

`calculate_fee(hours)` must follow these rules:

1. Hours must be a positive number (`int` or `float`, not `bool`). Invalid input returns `None`.
2. The **first hour is free**.
3. Each additional hour (including partial hours) is charged at **$10.00/hr**, with partial hours rounded **up**.
4. Fee for any 24-hour period is capped at **$80.00**.
5. For parking longer than 24 hours: charge the daily cap for each full day, plus the fee for the remaining hours.
6. Return the fee rounded to **2** decimal places.

### Fee examples

| Hours | Fee |
|-------|-----|
| 1 | $0.00 |
| 1.5 | $10.00 |
| 2 | $10.00 |
| 9 | $80.00 |
| 26 | $90.00 |

