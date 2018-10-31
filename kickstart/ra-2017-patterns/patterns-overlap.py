T = int(input())

for tc in range(0, T):
	boxA = list(input())
	boxB = list(input())

	boxI = boxA if len(boxA) > len(boxB) else boxB
	boxJ = boxB if len(boxA) > len(boxB) else boxA

	possible = True
	for i in range(0, len(boxI)):
		if i >= len(boxJ):
			if boxI[i] != "*":
				print("Ouch")
				possible = False
				break
		elif boxI[i] != boxJ[i] and boxI[i] != "*" and boxJ[i] != "*":
			print("Dang, ",boxI[i], boxJ[i])
			possible = False
			break

	print("Case #" + str(tc + 1) + ":", "TRUE" if possible else "FALSE")