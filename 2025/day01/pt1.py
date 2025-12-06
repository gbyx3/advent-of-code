import sys
input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split()
dial = 50
total = 0
print(f"Current dial possition: {dial}")
for rotation in lines:
    if rotation[0] == "L":
        dial = dial - int(rotation[1:])
        while dial < 0:
            dial = dial + 100

    if rotation[0] == "R":
        dial = dial + int(rotation[1:])
        while dial > 100:
            dial = dial - 100

    if dial == 100:
            dial = 0

    if dial == 0:
        total = total + 1
    print(f"Current dial possition after {rotation}: {dial}")

print(f"Total zeroes: {total}")

