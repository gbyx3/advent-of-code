import sys
input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split("\n")

i = 0
start = lines[i].index("S")
print(f"Starting at: {start}")
splits = 0
for line in lines[1:]:
    replace = []
    print(f"Current splits: {splits}")
    i = i +1
    replace = [ i for i, x in enumerate(line) if x == "^"]
    if len(replace) > 0:
        print(f"Adding: {len(replace)} from index: {replace}")
        splits = splits + len(replace)
        print(f"New splits: {splits}")
    else:
        print("No splits found.")
print(splits)
