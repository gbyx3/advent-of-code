import sys
input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split("\n")

i = 0
chart = []
start = lines[i].index("S")
print(f"Starting at: {start}")
print("Skiping first row")
splits = []
count = 0
for j, line in enumerate(lines):
    if j == 0:
        continue
    i = i +1
    spliters = [ i for i, x in enumerate(line) if x == "^"]
    print(f"Number of spliters on line {j}: {len(spliters)} at index: {spliters}")
    for s in spliters:
        print(f"Checking spliter at index: {s-1}, on line: {j+1}")
        print(f"Checking spliter at index: {s+1}, on line: {j+1}")
        if lines[j+1][s-1] != "^":
            print(f"Can split left at index: {s-1}, on line: {j+1}")
            lines[j+1] = lines[j+1][:s-1] + "|" + lines[j+1][s:]
        if lines[j+1][s+1] != "^":
            print(f"Can split right at index: {s+1}, on line: {j+1}")
            lines[j+1] = lines[j+1][:s+1] + "|" + lines[j+1][s:]

        if lines[j-1][s] == "|":
            print(f"Adding split at index: {s}, on line: {j}")
            splits.append(s)
            count = count + 1
    chart.append(line)


print('\n'.join(lines))
print("---")
#print('\n'.join(chart))




#    if len(replace) > 0:
#        print(f"Adding: {len(replace)} from index: {replace}")
#        splits = splits + len(replace)
#        print(f"New splits: {splits}")
#    else:
#        print("No splits found.")
print(splits)
print(len(splits))
