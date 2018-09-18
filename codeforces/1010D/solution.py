'''
D. Mars rover

Natasha travels around Mars in the Mars rover. But suddenly it broke down, namely — the logical scheme inside it. The scheme is an undirected tree (connected acyclic graph) with a root in the vertex 1, in which every leaf (excluding root) is an input, and all other vertices are logical elements, including the root, which is output. One bit is fed to each input. One bit is returned at the output.

There are four types of logical elements: AND (2 inputs), OR (2 inputs), XOR (2 inputs), NOT (1 input). Logical elements take values from their direct descendants (inputs) and return the result of the function they perform. Natasha knows the logical scheme of the Mars rover, as well as the fact that only one input is broken. In order to fix the Mars rover, she needs to change the value on this input.

For each input, determine what the output will be if Natasha changes this input.

Input
The first line contains a single integer n (2 < n < 10^6) — the number of vertices in the graph (both inputs and elements).
The i-th of the next n lines contains a description of i-th vertex: the first word "AND", "OR", "XOR", "NOT" or "IN" (means the input of the scheme) is the vertex type. If this vertex is "IN", then the value of this input follows (0 or 1), otherwise follow the indices of input vertices of this element: "AND", "OR", "XOR" have 2 inputs, whereas "NOT" has 1 input. The vertices are numbered from one.
It is guaranteed that input data contains a correct logical scheme with an output produced by the vertex 1.

Output
Print a string of characters '0' and '1' (without quotes) — answers to the problem for each input in the ascending order of their vertex indices.

Tests
(In this directory), 'cf test 1010 D solution.py'
'''

n = int(input())

# update fails on test 18
nodes = []
values = []
connections = []
for i in range(0, n):
	line = input().split(" ")
	nodes.append(line[0])
	values.append(int(line[1]) if line[0] == "IN" else -1)
	connections.append([int(j) - 1 for j in line[1:]] if line[0] != "IN" else [])


def computeGraph (i):
	inputs = connections[i]

	if nodes[i] == "IN":
		return values[i]
	elif nodes[i] == "AND":
		# get connections
		return computeGraph(inputs[0]) and computeGraph(inputs[1])
	elif nodes[i] == "OR":
		return computeGraph(inputs[0]) or computeGraph(inputs[1])
	elif nodes[i] == "XOR":
		return computeGraph(inputs[0]) ^ computeGraph(inputs[1])
	elif nodes[i] == "NOT":
		return not computeGraph(inputs[0])

results = []
for i in range(0, len(values)):
	if nodes[i] == "IN":
		values[i] = not values[i]
		results.append(str(int(computeGraph(0))))
		values[i] = not values[i]

print("".join(results))