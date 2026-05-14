## Marking instruction for Q1(a)(i)

Total: **3 marks**

Students are expected to complete the table and compare the final truth values of the two expressions.

The intended conclusion is:

**No. The truth values are different for rows 7 and 8.**

So the two expressions are **not equivalent**.

---

## Expected table

| Row | a | b | c | ~a | ~b | ~a ∧ ~b | (~a ∧ ~b) ∧ c | ~((~a ∧ ~b) ∧ c) | a ∨ c | (~a ∧ ~b) → (a ∨ c) |
| --: | - | - | - | -- | -- | ------- | ------------- | ---------------- | ----- | ------------------- |
|   1 | T | T | T | F  | F  | F       | F             | T                | T     | T                   |
|   2 | T | T | F | F  | F  | F       | F             | T                | T     | T                   |
|   3 | T | F | T | F  | T  | F       | F             | T                | T     | T                   |
|   4 | T | F | F | F  | T  | F       | F             | T                | T     | T                   |
|   5 | F | T | T | T  | F  | F       | F             | T                | T     | T                   |
|   6 | F | T | F | T  | F  | F       | F             | T                | F     | T                   |
|   7 | F | F | T | T  | T  | T       | T             | F                | T     | T                   |
|   8 | F | F | F | T  | T  | T       | F             | T                | F     | F                   |

---

## Marks allocation

| Item                  | Marks | Mark type | What to award for                              |
| --------------------- | ----: | --------- | ---------------------------------------------- |
| `~a ∧ ~b`             |   0.5 | Method    | Correctly combines `~a` and `~b` using AND     |
| `~((~a ∧ ~b) ∧ c)`    |     1 | Accuracy  | Correct final truth values for this expression |
| `a ∨ c`               |   0.5 | Method    | Correctly combines `a` and `c` using OR        |
| `(~a ∧ ~b) → (a ∨ c)` |     1 | Accuracy  | Correct final truth values for this expression |

---

## Key comparison

| Row | `~((~a ∧ ~b) ∧ c)` | `(~a ∧ ~b) → (a ∨ c)` | Same? |
| --: | ------------------ | --------------------- | ----- |
|   1 | T                  | T                     | Yes   |
|   2 | T                  | T                     | Yes   |
|   3 | T                  | T                     | Yes   |
|   4 | T                  | T                     | Yes   |
|   5 | T                  | T                     | Yes   |
|   6 | T                  | T                     | Yes   |
|   7 | F                  | T                     | No    |
|   8 | T                  | F                     | No    |

---

## Final answer to accept

Accept any answer with the same meaning as:

> No. The truth values are different for rows 7 and 8.

Do not require the exact wording. Award the conclusion if the student clearly says that the two expressions are **not equivalent** and identifies the mismatch in **rows 7 and 8**.
