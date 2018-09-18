
def bfmaxSubarray (arr):
	m = 0
	for i in range(0, len(arr)):
		for j in range(i, len(arr)):
			print "summing ", arr[i:j + 1]
			v = sum(arr[i:j + 1])
			m = max(v, m)

	return m


print "bf max: ", bfmaxSubarray([-1, -2, 0, 1, -1, 2, -2])
