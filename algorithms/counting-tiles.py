
def solve (r, m, grid):
	if r == m:
		'''print("SOLUTION")
		for i in range(0, m):
			print(grid[i])
		print("")'''
		return 1
	# enumerate all possibilites for this row
	candidates = []
	def generateCol (n, r, m, ls, i = 0):
		if i == n:
			candidates.append([a for a in ls])
			return
		ps = ["c", "n", "u"]
		if i == 0 and "b" in ps:
			ps.remove("b")
		elif i == n - 1 and "c" in ps:
			ps.remove("c")
		
		if i > 0 and ls[i - 1] == "c":
			ps = ["b"]
		if r == 0 and "u" in ps:
			ps.remove("u")
		elif r == m - 1 and "n" in ps:
			ps.remove("n")

		for p in ps:
			ls[i] = p
			generateCol(n, r, m, ls, i + 1)

	generateCol(len(grid[r]), r, m, ["" for i in range(0, len(grid[r]))])

	# check possibilities against above row
	def isValidRow (row):
		for i in range(0, len(grid[r])):
			if grid[r - 1][i] == "n" and row[i] != "u":
				return False
			if row[i] == "u" and grid[r - 1][i] != "n":
				return False
		return True


	if r > 0:
		candidates = filter(isValidRow, candidates)

	poss = 0
	for candidate in candidates:
		grid[r] = candidate
		poss += solve(r + 1, m, grid)

	return poss

g = [["" for j in range(0, 5)] for i in range(0, 8)]
print(solve(0, len(g), g))
