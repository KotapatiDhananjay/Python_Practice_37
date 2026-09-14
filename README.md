# Python Regex - Dot (`.`) Character 🔎

A simple Python program demonstrating how the **`.` (dot)** character works in Regular Expressions.

## 📌 Description

This example demonstrates:

* Matching digits using `[0-9]`
* Using `.` to match any character
* Combining character classes with `.`
* Using `re.search()` to find patterns in strings

## 💻 Code

```python
import re

message = "The current Python version is 3.13. Other previous versions are 3.12, 3.11, 3.10."

# Match two consecutive digits
match_obj = re.search("[0-9][0-9]", message)
print(match_obj)


# Match two consecutive digits in another string
match_obj = re.search("[0-9][0-9]", "House number: 251/A")
print(match_obj)


# Match:
# digit + any character + two digits
match_obj = re.search("[0-9].[0-9][0-9]", message)
print(match_obj)


# . matches any character except a newline
message_1 = "The year is 2026"

match_obj = re.search("[0-9].[0-9][0-9]", message_1)
print(match_obj)
```

## 🧠 Key Concept: Dot (`.`)

In Regular Expressions, the dot `.` is a **special character**.

It matches **any single character except a newline (`\n`)**.

For example:

```python
r"."
```

can match:

```text
A
5
@
space
.
```

but it does not normally match a newline.

## 🔍 Understanding the Pattern

Consider:

```python
r"[0-9].[0-9][0-9]"
```

This pattern means:

```text
[0-9]     → One digit
.         → Any single character
[0-9]     → One digit
[0-9]     → One digit
```

So it looks for:

```text
Digit + Any Character + Two Digits
```

### Example

In:

```text
3.13
```

the pattern matches:

```text
3.13
```

because:

```text
3 → [0-9]
. → .
1 → [0-9]
3 → [0-9]
```

## 📌 `[0-9]` vs `.`

| Pattern            | Meaning                                     |
| ------------------ | ------------------------------------------- |
| `[0-9]`            | Matches one digit                           |
| `.`                | Matches any single character except newline |
| `[0-9][0-9]`       | Matches two consecutive digits              |
| `[0-9].[0-9][0-9]` | Digit + any character + two digits          |

## 🔎 `re.search()`

The program uses:

```python
re.search(pattern, string)
```

It searches for the **first occurrence** of the given pattern anywhere in the string.

If a match is found, it returns a `Match` object.

If no match is found, it returns:

```text
None
```

## 🖥️ Example

For:

```text
The current Python version is 3.13.
```

The pattern:

```python
"[0-9].[0-9][0-9]"
```

can match:

```text
3.13
```

Here the `.` in the regex matches the actual `.` between `3` and `13`.

## 🛠️ Technologies Used

* Python 3
* `re` module
* Regular Expressions

## ▶️ How to Run

Save the program as:

```text
regex_dot.py
```

Run:

```bash
python regex_dot.py
```

## 📚 Learning Outcome

This example helps understand:

* `re.search()`
* Character classes
* `[0-9]`
* Dot (`.`) in Regex
* Combining Regex patterns
* Match objects

## 👨‍💻 Author

**Kotapati Dhananjay**
