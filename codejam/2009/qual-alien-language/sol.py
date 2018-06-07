import re
print "START"
#f = open("codejam/2009/qual-alien-language/sample.txt", "r")
#f = open("codejam/2009/qual-alien-language/A-small-practice.in.txt", "r")
f = open("codejam/2009/qual-alien-language/A-large-practice.in.txt", "r")
o = open("codejam/2009/qual-alien-language/output.txt", "w")
L, D, N = [int(i) for i in f.readline().split(" ")]
# L = number of tokens per word
# D = number of words in vocabulary
# N = number of test cases

vocab = [f.readline().strip() for i in range(0, D)]
cases = [f.readline().strip() for i in range(0, N)]

def solveIt (vocab, tokens, w, i):
    if len(w) == L:
        return [w]

    candidates = [w + c for c in tokens[i]]
    accepted = []
    for candidate in candidates:
        for j in vocab:
            if candidate == j[0:len(candidate)]:
                accepted += solveIt([j], tokens, candidate, i + 1)
    return accepted

for t in range(0, len(cases)):
    print "test case " + str(t)
    word = cases[t]
    if "(" not in word:
        ans = 1 if word in vocab else 0
        o.write("Case #" + str(t + 1) + ": " + str(ans) + "\n")
        continue

    tokens = []
    group = []
    paren = False
    for c in word:
        if paren and c != ")":
            group.append(c)
        elif paren and c == ")":
            tokens.append(group)
            group = []
            paren = False
        elif not paren and c != "(":
            tokens.append([c])
        elif not paren and c == "(":
            paren = True

    ans = len(set(solveIt(vocab, tokens, "", 0)))
    o.write("Case #" + str(t + 1) + ": " + str(ans) + "\n")
