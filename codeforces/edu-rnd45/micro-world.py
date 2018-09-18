# n is the number of bacteria
# Find minimum surviving bacteria if any ith bacteria can eat jth bacteria if a[i] > a[j] and a[i] <= a[j] + K

# Solution: frequency list, sort by a[x][0], then eliminate all bacteria by criteria above for a[i] and a[i - 1] as i increases.

n, K = [int(s) for s in raw_input().split(" ")]
bacteria = [int(s) for s in raw_input().split(" ")]


def loop_freq (ls):
    freq = {}
    for b in bacteria:
        if b in freq:
            freq[b] += 1
        else:
            freq[b] = 1
    return freq.iteritems()

bacteria = [[k, v] for k, v in loop_freq(bacteria)]
bacteria = sorted(bacteria, key=lambda x: x[0])
living = [True for b in bacteria]

for i in range(1, len(bacteria)):
    if bacteria[i][0] > bacteria[i - 1][0] and bacteria[i][0] <= bacteria[i - 1][0] + K:
        living[i - 1] = False

print sum([bacteria[i][1] for i in range(0, len(bacteria)) if living[i]])
