# Python_Fundamentals

Practice programs for Module 2, Assignment 1. Python 3.x only.

## Programs

### presidents.py
Displays the first N U.S. presidents (from the first ten), with an
asterisk next to any president whose last name starts with A.
Run: `python presidents.py`
Then enter a number from 1 to 10 when prompted. The list prints once
with a for loop and once with a while loop, followed by a count of
the asterisked names.

### simple_interest.py
Calculates simple interest using SI = (P x R x T) / 100.
Run: `python simple_interest.py`
Then enter the principal amount, the rate of interest as a
percentage (enter 5 for 5%, not 0.05), and the time in years.

## Assumptions
- presidents.py covers the first ten U.S. presidents only; entering
  a number outside 1-10 is rejected and the prompt repeats.
- simple_interest.py accepts decimal inputs for all three values;
  negative values are rejected and the prompt repeats.
- The rate is entered as a percentage (5 means 5%).

## Edge cases tested
- presidents.py: entering "abc" prints a friendly message and asks
  again instead of crashing; entering 10 prints all ten presidents
  with 2 asterisked names (John Adams, John Quincy Adams).
- simple_interest.py: entering "abc" prints a friendly message and
  asks again; entering -500 is rejected as negative and the prompt
  repeats; 1000, 5, 2 correctly gives $100.00.
