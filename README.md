# CIE-Computer-Science-Pre-release-2019
A solution to the CIE GCSE Computer Science Pre-release problem written in Python 3.x.

# solution.py
- Includes tasks 1, 2 & 3 with comments.
- Uses: try-except, enumerate, filter, continue, index, isdigit, lambdas, max

### Task 3 explanation
```
index = daynames.index(day[:3]) + (int(day[-1])-1)*5
```
- The input (e.g. Tue2) needs to be converted into an index in an array (e.g. Tue2 -> 6), as the data is stored in a 20 day list rather than 4 weeks of 5 days each
1. So the input is separated into the day (i.e. Tue) and the week (i.e. 2)
2. Then the day position is found out (i.e. Mon = 0, Tue = 1 ...)
3. Counting in base 5 (substituting for weeks and days), this is used as the units column
4. The week number therefore is used as the 10s column
5. Since arrays start from 0, not 5, the week number is decremented and then multiplied by 5
6. The two values and then added to give the final position in the list

# oneliner.py
- Consists of one line of code which runs the whole program
- I have included the input dataset under input.txt
- Uses: exec, split, recursion, map, isdigit, list comprehensions, enumerate, f-strings
- Requires python 3.6+ due to f-strings
