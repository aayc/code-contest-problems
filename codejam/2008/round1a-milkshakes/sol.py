n = int(input())

def couple (ls):
	return [[ls[i], ls[i + 1]] for i in range(0, len(ls), 2)]

def solveMe (customers, i, malted, isSet):
	if i == len(customers):
		return sum(malted)

	customer = customers[i]
	results = []
	maltedPreference = [pref for pref in customer if pref[1] == 1] # should return [] of length 0 or 1

	if len(maltedPreference) > 0:
		print(maltedPreference, isSet)
		if isSet[maltedPreference[0][0] - 1] and malted[maltedPreference[0][0] - 1] == 0:
			return -1
		else:
			malted[maltedPreference[0][0] - 1] = 1
			isSet[maltedPreference[0][0] - 1] = True
			return solveMe(customers, i + 1, malted, isSet)
	else:
		if all([malted[p[0] - 1] != p[1] for p in customer]):
			return -1
		else:
			return solveMe(customers, i + 1, malted, isSet)

			'''
	for preference in customer:
		# preference is a pair
		if preference[1] == 0 and malted[preference[0] - 1] == 1:
			continue

		if preference[1] != malted[preference[0] - 1] and isSet[preference[0] - 1]:
			continue

	
		past_malted = malted[preference[0] - 1]
		malted[preference[0] - 1] = preference[1]
		isSet[preference[0] - 1] = True
		results.append(solveMe(customers, i + 1, malted, isSet))
		malted[preference[0] - 1] = past_malted
		isSet[preference[0] - 1] = False

	return min(results) if len(results) > 0 else -1
	'''

for T in range(0, n):
	num_flavors = int(input())
	num_customers = int(input())
	customers = []
	for i in range(0, num_customers):
		line = [int(x) for x in input().split(" ")]
		num_pairs = line.pop(0)
		customers.append(couple(line))

	customers = sorted(customers, key=len)
	print(customers)
	# backtracking
	
	ans = solveMe(customers, 0, [0 for m in range(0, num_flavors)], [False for m in range(0, num_flavors)])


	print("Case #" + str(T + 1) + ":", (ans if ans != -1 else "IMPOSSIBLE"))