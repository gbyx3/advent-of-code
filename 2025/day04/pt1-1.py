import sys


input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split()


print(f"Number of lines in file: {len(lines)}")
total_lines = len(lines)
move_this = 0
for lane_pos, lane in enumerate(lines):

    # Dont print the lane "above" the first lane
    if lane_pos != 0:
        print(lines[lane_pos -1])
    print(f"--- Current lane ( {lane_pos} )---")
    print(lane)
    print("------")
    # Dont print the lane after the last lane
    if lane_pos != total_lines -1:
        print(lines[lane_pos +1])
    last_ball = int(len(lane))
    for ball_pos, ball in enumerate(lane):
        print(f"{ball_pos=}")
        adjacent_balls = 0
        # Only look at "balls"
        if ball_pos == last_ball:
            print("Last ball on the row")
        if  ball != "@":
            continue

        # Find left and right balls, if you arent ant first or last index
        left_space = ball_pos - 1
        right_space = ball_pos + 1
        if ball_pos > 0:
            bl = lane[left_space]
            if bl == "@":
                adjacent_balls = adjacent_balls +1
                print(f"Ball to left: {bl}")
        if ball_pos != last_ball -1:
            br = lane[right_space]
            if br == "@":
                adjacent_balls = adjacent_balls +1
                print(f"Ball to right: {br}")

        # Find over under balls
        up_space = lane_pos -1
        down_space = lane_pos +1

        if lane_pos != 0:
            ba = lines[up_space][ball_pos]
            if ba == "@":
                adjacent_balls = adjacent_balls +1
                print(f"Ball above: {ba}")
            if ball_pos != last_ball -1:
                bar = lines[up_space][right_space]
                if bar == "@":
                    adjacent_balls = adjacent_balls +1
                    print(f"Ball above right: {bar}")
            bal = lines[up_space][left_space]
            if bal == "@":
                adjacent_balls = adjacent_balls +1
                print(f"Ball above left: {bal}")
        if lane_pos < total_lines -1:
            bu = lines[down_space][ball_pos]
            if bu == "@":
                adjacent_balls = adjacent_balls +1
                print(f"Ball under: {lines[down_space][ball_pos]}")
            bul = lines[down_space][left_space]
            if bul == "@":
                adjacent_balls = adjacent_balls +1
                print(f"Ball under left: {bul}")
            if ball_pos != last_ball -1:
                bur = lines[down_space][right_space]
                if bur == "@":
                    adjacent_balls = adjacent_balls +1
                    print(f"Ball under right: {bur}")
        if adjacent_balls < 4:
            print(f"Ball: {ball} is in position: {ball_pos}, on lane: {lane_pos} and has adjacent balls: {adjacent_balls}")
            move_this = move_this +1
    if lane_pos == total_lines:
        print(f"Last line done: {lane_pos}")
print(f"Move {move_this}, number of balls")

