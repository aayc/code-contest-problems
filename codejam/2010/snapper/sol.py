N = int(input())

for T in range(0, N):
    n, k = [int(x) for x in input().split(" ")]
    snappers = ["0" for i in range(0, n)]
    power = ["0" for i in range(0, n)]
    mask = ["1" for i in range(0, n)]
    power[0] = "1"

    power = int("".join(power), 2)
    mask = int("".join(mask), 2)
    snappers = 0
    
    print(power, mask) 
    # 
    print(bin(power ^ snappers ^ mask))
