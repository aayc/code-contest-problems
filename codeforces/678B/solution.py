'''
B. The Same Calendar

The girl Taylor has a beautiful calendar for the year y. In the calendar all days are given with their days of week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.

The calendar is so beautiful that she wants to know what is the next year after y when the calendar will be exactly the same. Help Taylor to find that year.

Note that leap years has 366 days. The year is leap if it is divisible by 400 or it is divisible by 4, but not by 100 (https://en.wikipedia.org/wiki/Leap_year).

Input
The only line contains integer y (1000 ≤ y < 100'000) — the year of the calendar.

Output
Print the only integer y' — the next year after y when the calendar will be the same. Note that you should find the first year after y with the same calendar.

Tests
(In this directory), 'cf test 678 B solution.py'
'''

def is_leap (y):
	return (y % 400 == 0 or y % 4 == 0) and not y % 100 == 0

y_p = 0
y_i = y + 1
while y_p == 0:
	