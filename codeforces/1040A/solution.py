# Python 2.7
# Accepted

n, w, b = map(int, raw_input().split(" "))
dancers = map(int, raw_input().split(" "))

cost = 0
bad = False
for i in range(0, n / 2):
	l = dancers[i]
	r = dancers[n - i - 1]
	if l != r:
		if l == 2 and r != 2:
			cost += w if r == 0 else b
		elif r == 2 and l != 2:
			cost += w if l == 0 else b
		else:
			# they just don't match and they are both set.
			cost = -1
			bad = True
			break
	elif l == 2 and r == 2:
		cost += min(w, b) * 2

if len(dancers) % 2 != 0 and not bad:
	# get middle
	# if middle is already something then 0
	cost += 0 if dancers[n / 2] != 2 else min(w, b)

print(cost)
