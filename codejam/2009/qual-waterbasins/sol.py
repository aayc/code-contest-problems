f = open("codejam/2009/qual-waterbasins/sample.txt", "r")

def labelBasins (R, C, map):
    pass

T = int(f.readline())

for i in range(0, T):
    R, C = [int(j) for j in f.readline().split(" ")]
    #print f.readline().strip().split(" ")
    map = [map(lambda x: int(x), f.readline().strip().split(" ")) for j in range(0, R)]
    print R, C, map
