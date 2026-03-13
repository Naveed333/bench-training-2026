## Day 1 — Data Types, Control Flow & Loops

Built three scripts: variables + f-string output with retirement and coffee budget calculations; a `grade_classifier()` function (Distinction/Pass/Fail) looped over a score list without repeating if-else; and a multiplication table generator with a `while True` input validation loop and a bonus that prints all 12 tables. The trickiest part was the `while True` re-prompt — without `ValueError` handling, a non-integer input crashes the program. Next time I'd wrap `int(input())` in a `try/except` from the start.
