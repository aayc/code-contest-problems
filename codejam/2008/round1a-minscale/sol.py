n = int(input())
for T in range(0, n):
	v_len = int(input())
	a = list(map(int, input().split(" ")))
	b = list(map(int, input().split(" ")))

	a_sorted = sorted(a)
	b_sorted = sorted(b, reverse=True)
	ans = sum([x[0] * x[1] for x in zip(a_sorted, b_sorted)])
	print("Case #" + str(T + 1) + ":",ans)