'''
coinValues {25,15,1, 3} where V = 30
25, 1 1 1 1 1
15, 15

min to find total 1? 1
min to find total 2? 2
min to find total 3? 1
min to find total 4?
	min to find total of n = minimum ( min(n - coinValues[i]) + 1, 
										min(n - coinValues[i + 1]) + 1,
										 ... coinValues[length]))
min(4 - 25)
min(4 - 15)
min(4 - 3) + 1 -> min(1) + 1 -> 1 + 1 -> 2
min(4 - 1) -> min(3) + 1 -> 1 + 1 -> 2

min(5 - 25) + 1
min(5 - 15) + 1
min(5 - 3) + 1 -> min(2) + 1 -> 2 + 1 -> 3
min(5 - 1) + 1 -> min(4) + 1 -> 2 + 1 -> 3

min(30 - 25) -> min(5) + 1 -> 3 + 1 = 4 coins
min(30 - 15) + 1 -> min(15) + 1 -> 2
min(30 - 3) + 1 -> min(27) + 1 -> 3 + 1 = 4
min(30 - 1) + 1 -> min(29) + 1 -> 5 + 1 = 6
'''

coinValues = [25, 15, 3, 1]
total = 30

dp_array = [-1 for x in range(0, 31)]
dp_array[0] = 0

for i in range(1, len(dp_array)):
	dp_array[i] = min([dp_array[i - coinValue] + 1 for coinValue in coinValues if i - coinValue >= 0])

print(dp_array[29]) #25, 3, 1