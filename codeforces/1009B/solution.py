'''
B. Minimum Ternary String

You are given a ternary string (it is a string which consists only of characters '0', '1' and '2').

You can swap any two adjacent (consecutive) characters '0' and '1' (i.e. replace "01" with "10" or vice versa) or any two adjacent (consecutive) characters '1' and '2' (i.e. replace "12" with "21" or vice versa).

For example, for string "010210" we can perform the following moves: 

  "010210" \rightarrow "100210";  "010210" \rightarrow "001210";  "010210" \rightarrow "010120";  "010210" \rightarrow "010201". 

Note than you cannot swap "02" \rightarrow "20" and vice versa. You cannot perform any other operations with the given string excluding described above.

You task is to obtain the minimum possible (lexicographically) string by using these swaps arbitrary number of times (possibly, zero).

String a is lexicographically less than string b (if strings a and b have the same length) if there exists some position i (1 < i < |a|, where |s| is the length of the string s) such that for every j < i holds a_j = b_j, and a_i < b_i.

Input
The first line of the input contains the string s consisting only of characters '0', '1' and '2', its length is between 1 and 10^5 (inclusive).

Output
Print a single string — the minimum possible (lexicographically) string you can obtain by using the swaps described above arbitrary number of times (possibly, zero).

Tests
(In this directory), 'cf test 1009 B solution.py'
'''
s = list(input())

'''
Failed solution: tried a greedy algorithm to bring 1s left, then 0s left.
def bringForward (c, switcher):
	for i in range(1, len(s)):
		if s[i] == c and s[i - 1] == switcher:
			# move it back
			quit = False
			for j in range(i - 1, -1, -1):
				if s[j] == switcher:
					continue
				else:
					s[j + 1] = c
					s[i] = switcher
					quit = True
					break
			if not quit:
				s[0] = c
				s[i] = switcher
bringForward("1", "2")
bringForward("0", "1")
print("".join(s))
'''

# Solution: notice that "1"s can move anywhere in string s.  Remove all 1s and place them to the left of the first 2.
num1s = 0
for i in range(0, len(s)):
	if s[i] == "1":
		num1s += 1
s = list(filter(lambda x: x != "1", s))
for i in range(0, len(s)):
	if s[i] == "2":
		s.insert(i, "1" * num1s)
		break
print("".join(s))