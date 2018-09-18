def turn (r):
	return [r[1], r[0]]

n = input()
rectangles = [[rect[0], rect[1]] for rect in [map(lambda x: int(x), raw_input().split(" ")) for i in range(0, n)]]

if rectangles[0][0] > rectangles[0][1]:
	rectangles[0] = turn(rectangles[0])

for i in range(1, n):
	# the max(r[0], r[1]) < previous r[1]
	if max(rectangles[i][0], rectangles[i][1]) <= rectangles[i - 1][1]:
		rectangles[i][1] = max(rectangles[i][0], rectangles[i][1])
	else:
		if min(rectangles[i][0], rectangles[i][1]) <= rectangles[i - 1][1]:
			rectangles[i][1] = min(rectangles[i][0], rectangles[i][1])
		else:
			print("NO")
			exit(1)
print("YES")

# Runtime error, but not sure why.