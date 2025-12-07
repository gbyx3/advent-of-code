import sys


def is_roll(r):
    global count
    if r == "@":
        count = count +1


input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split()
print(f"Number of lines in file: {len(lines)}")
total_lines = len(lines)
move_this = 0
for i, lane in enumerate(lines):
    for j, roll in enumerate(lane):
        count = 0
        if roll != "@":
            continue
        print(f"Checking roll at: {j}, on lane {i}, value: {roll}")
        if i != 0:
            print("Looking up")
            print(f"{lines[i-1][j]}")
            is_roll(lines[i-1][j])
            if j != 0:
                print("Looking up left")
                print(f"{lines[i-1][j-1]}")
                is_roll(lines[i-1][j-1])
            if j != len(lane) -1:
                print("Looking up right")
                print(f"{lines[i-1][j+1]}")
                is_roll(lines[i-1][j+1])
        else:
            print("First line, no up")

        if i != total_lines -1:
            print("Looking down")
            print(f"{lines[i+1][j]}")
            is_roll(lines[i+1][j])
            if j != 0:
                print("Looking down left")
                print(f"{lines[i+1][j-1]}")
                is_roll(lines[i+1][j-1])
            if j != len(lane) -1:
                print("Looking down right")
                print(f"{lines[i+1][j+1]}")
                is_roll(lines[i+1][j+1])
        else:
            print("Last line, no down")

        if j != 0:
            print("Looking left")
            print(f"{lane[j-1]}")
            is_roll(lane[j-1])
        else:
            print("First roll, no left")

        if j != len(lane) -1:
            print("Looking right")
            print(f"{lane[j+1]}")
            is_roll(lane[j+1])
        else:
            print("Last roll, no right")

        if count < 4:
            print(f"Move roll at {j} on lane {i}, has adjacent rolls: {count}")
            move_this = move_this +1
        else:
            print(f"Roll at {j} on lane {i} is surrounded with {count} adjacent rolls, wont move")
print(f"Move {move_this}, number of balls")

