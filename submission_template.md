# AI Code Review Assignment (Python)

## Candidate
- Name: Bengisu Karaca
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function counts all orders with `len(orders)` but only sums non-cancelled orders, which results in an incorrect average calculation
- When the orders list is empty or contains only cancelled orders, the function will crash with a ZeroDivisionError


### Edge cases & risks
- No handling for empty input lists
- No validation that orders are dictionaries or contain required fields 
- Assumes 'amount' values are always numeric without type checking
- No handling for None values or missing keys, which will cause KeyError
- All cancelled orders scenario will cause division by zero


### Code quality / design issues
- Missing input validation and error handling
- Assumes perfect input data


## 2) Proposed Fixes / Improvements
### Summary of changes
- fixed the count to only include non-cancelled orders
- added input validation (empty list, dictionary structure, field existence)
- added type validation for amounts
- implemented division by zero protection by checking count before dividing
- made function skip invalid entries


### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would test  valid inputs first to confirm correct averaging, then focus on edge cases such as all orders being cancelled, an empty order list, and orders with zero or negative amounts to check handling and division-by-zero protection. I’d also include invalid entries (missing fields, wrong types, non-dictionaries) to verify they are skipped safely

I tested both task1.py and correct_task1.py using dataset of 21 cases. correct_task1.py passed 21/21 tests, while task1.py passed only 7/21, mainly failing on edge cases like all cancelled orders, empty lists, invalid entries, and zero or negative amounts. This was a small self-designed test to compare robustness and correctness.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- States it divides by "the number of orders" when the code actually divides by (all orders), not the count of non-cancelled orders
- Says it "correctly excludes cancelled orders" but the implementation is incorrect due to the count
- No mention of edge cases, error handling, or input assumptions

### Rewritten explanation
This function calculates  average order value by summing the amounts of all non-cancelled orders and dividing by the count of non-cancelled orders. The function validates that each order is a dictionary containing both 'status' and 'amount' fields, ensures amounts are numeric, and filters out cancelled orders. It handles edge cases including empty lists, all orders being cancelled, missing or invalid fields, non-numeric amounts, and division by zero, returning 0.0 in cases where no valid non-cancelled orders exist.


## 4) Final Judgment
- Decision: Reject
- Justification: The original function contains critical bugs that produce incorrect results and will crash on common edge cases. The explanation is incorrect and claims the function works correctly when it doesn't.

- Confidence & unknowns: High confidence in the rejection. The bugs are clear. Some open questions remain around edge case behavior (return 0.0, None, or raise an exception?) and whether negative amounts are valid, but the implementation has fundamental issues.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- only checks for '@' symbol and accepts invalid emails like "@", "@@", "@gmail.com", "user@", "not email @ mail"
- it will crash with TypeError if the list  non-string items because 'in' operator requires a string
- not handles empty list

### Edge cases & risks
- no validation for email format, missing local part, domain or proper structure
- accepts emails with multiple '@' symbols ("user@@gmail.com")
- accepts emails without domain extensions ("user@gmail"),
- not handles whitespace (" user@gmail.com ", "user @gmail.com")
- accepts empty strings or strings with only '@' as valid

### Code quality / design issues
- no input validation for list items
- no proper email validation using regex or established patterns
- no clear definition of what constitutes a "valid" email

## 2) Proposed Fixes / Improvements
### Summary of changes
- added proper email validation using regex pattern that checks for basic email structure (local@domain format)
- added input validation to handle empty lists and non-string items 
- made function defensive by skipping invalid entries rather than crashing




### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would focus on testing common valid email formats first, then test boundary conditions such as the maximum allowed local-part length (64 characters) and total email length (254 characters)
Then, I would test dot related edge cases, leading, trailing, and consecutive dots.
And test clearly invalid formats like missing or multiple '@' symbols and whitespace, to ensure the regex fails safely.


I tested both task2.py and correct_task2.py using dataset of 35 cases. correct_task2.py passed 35/35 tests, while task2.py passed only 13/35, mainly failing on edge cases like double dots, whitespace, and format boundaries. This was a small self-designed test to compare robustness and correctness.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- it claims validating emails when it only checks for "@" symbol, which is insufficient validation and accepts many obviously invalid emails
- it says it "safely ignores invalid entries" but it will crash on non-string types (doesn't handle TypeError)

### Rewritten explanation
- This function counts the number of valid email addresses in the input list. It validates emails using regular expression validation. The function handles edge cases including empty lists, non-string items, malformed emails , whitespace. Function  processes imperfect data without crashing and returns an accurate count of structurally valid email addresses.


## 4) Final Judgment
- Decision: Reject
- Justification: The original function has broken validation mechanism that only checks for "@" presence, accepting invalid emails like "@", "@@domain.com", or "user@". The explanation claims the function "safely ignores invalid entries" when it will crash with TypeError on None or numeric values. The implementation fails to meet basic requirements for email validation and lacks the error handling described in its documentation.

- Confidence & unknowns: High confidence in rejection. The bugs are clear. Some open questions remain around exact requirements, such as whether internationalized domains or Unicode characters should be supported, how strict the validation needs to be, and whether uppercase letters are acceptable. These details don't change the outcome, as the current implementation  fails to meet basic requirements.


---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function counts all values with `len(values)` but only sums non-None values, resulting in an incorrect average calculation (same issue as Task 1)
- When the values list is empty or contains only None values, the function will crash with a ZeroDivisionError (same issue as Task 1)
- The `float(v)` conversion will crash with ValueError on non-numeric strings and TypeError on unconvertible types


### Edge cases & risks
- Empty input list causes division by zero crash
- No  type checking before float conversion
- Crashing on common invalid values like N/A, "", invalid
- All-None input causes division by zero since count never increments
- No handling for special float values (infinity, NaN)
- Assumes all non-None values are numeric without any validation


### Code quality / design issues
- No input validation and error handling
- No try-except around type conversion 
- Claims to handle "mixed input types" but crashes on many common types

## 2) Proposed Fixes / Improvements
### Summary of changes
- It counts only valid numeric values
- Checks for empty lists
- Safely converts values to float using try-except
- Protects against division by zero
- Skips None values before conversion
- Handles special float values like infinity and NaN

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would focus on testing lists containing valid numeric values, a mix of valid numbers and None values, and lists with all valid numbers to ensure the average is calculated correctly under normal conditions. Then, I would test edge cases like empty lists, lists with all None values, single-value lists, and mixes of integers and floats, to confirm the function handles boundaries safely and returns 0.0 when appropriate.
Next, I would test type validation, I would also include special float values like inf, nan

 I tested both task3.py and correct_task3.py using dataset of 35 cases. correct_task3.py passed 20/20 tests, while task3.py passed only 11/20, mainly failing on edge cases like empty lists, cancelled or invalid entries, zero and negative amounts. This was a small self-designed test to compare robustness and correctness.



## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- states it divides by "the remaining values" but the code divides by (all values), not the count of valid values
- Claims it "safely handles mixed input types" but will crash with ValueError/TypeError on non-numeric strings or objects
- No mention of what happens with empty lists, or division by zero



### Rewritten explanation
- This function calculates the average of valid numeric measurements, then dividing the sum by the count of valid values only. The function validates each value by attempting to convert it to a float. It handles edge cases including empty lists, all None or invalid values, mixed numeric types (integers and floats), and division by zero protection. The function uses try-except error handling to skip invalid entries without crashing.


## 4) Final Judgment
- Decision: Reject
- Justification: The original code contains the same critical count mismatch bug as Task 1, producing mathematically incorrect averages. It also crashes with non-numeric strings, empty lists while it claims "safely handle mixed input types" and "ensure accurate average." The implementation  fails to deliver on its documented promises.

- Confidence & unknowns: High confidence in rejection. The bugs are clear. Some open questions remain around whether numeric strings like "123.45" should convert, how to handle infinity and NaN, and whether zero is a valid measurement, but the implementation is broken regardless.

