n = int(input())
# max - 20 times,
# 24 * 60 = 1440

# loop from 1 to 1440
#
# 
def flatten (ls):
	return [item for sublist in ls for item in sublist]

def couple (ls):
	return [[ls[i], ls[i + 1]] for i in range(0, len(ls), 2)]

for T in range(0, n):
	turnaround = int(input())
	NA, NB = list(map(int, input().split(" ")))
	arrivals_raw = [input() for i in range(0, NA)]
	aToB = couple(list(map(lambda time_s: int(time_s.split(":")[0])*60 + int(time_s.split(":")[1]), flatten(map(lambda x: x.split(" "), arrivals_raw)))))
	depts_raw = [input() for j in range(0, NB)]
	bToA = couple(list(map(lambda time_s: int(time_s.split(":")[0])*60 + int(time_s.split(":")[1]), flatten(map(lambda x: x.split(" "), depts_raw)))))

	aToB = list(map(lambda x: [x[0], x[1] + turnaround], aToB))
	bToA = list(map(lambda x: [x[0], x[1] + turnaround], bToA))

	#print(aToB)
	#print(bToA)

	a_trains_total = 0
	b_trains_total = 0
	a_trains = 0
	b_trains = 0

	for m in range(0, 1440):
		# if there is some aToB that's leaving right now and a_trains is 0
		happened = False
		for trip in aToB:
			if trip[1] == m:
				happened = True
				# train arrived at station B
				b_trains += 1

		for trip in bToA:
			if trip[1] == m:
				happened = True
				# train is arriving at station A
				a_trains += 1

		for trip in aToB:
			if trip[0] == m:
				happened = True
				# train is leaving station A
				if a_trains == 0:
					a_trains_total += 1
				else:
					a_trains -= 1
				pass

		for trip in bToA:
			if trip[0] == m:
				happened = True
				if b_trains == 0:
					b_trains_total += 1
				else:
					b_trains -= 1
				# train is leaving station B
				pass
		if happened:
			pass
			#print(m, a_trains, b_trains, a_trains_total, b_trains_total)
	print("Case #" + str(T + 1) + ":",a_trains_total, b_trains_total)
