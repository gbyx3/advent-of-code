import sys
input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split()
l = []
for line in lines:
    numbers = [i for i in line]
    f = "0"
    for i, x in enumerate(numbers):
        if x > f and i != len(numbers) -1:
            f = x
            n = i
            #print(f"Replacing first bat with {x} in possition {i}")
    del numbers[:n+1]
    s = max(numbers)
    l.append(int(f+s))
print(f"The Joltage is: {sum(l)}")




