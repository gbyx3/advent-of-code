import sys
import math
input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split("\n")
len_lines = len(lines)
l = []
num_stores = len(lines[0].split())
data = {}
for s in range(0, num_stores):
    data[s] = []
for j in lines:
    for i, n in enumerate(j.split()):
        data[i].append(n)

for i, stuff in data.items():
    op = stuff[-1]
    del stuff[-1]
    ints = [int(x) for x in stuff]
    if op == '+':
        l.append(sum(ints))
    if op == '*':
        l.append(math.prod(ints))
print(f"The Cephalopod sum is: {sum(l)}")
