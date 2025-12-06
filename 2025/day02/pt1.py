import sys
input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split(',')
l = []
for corrupt in lines:
    seq = corrupt.split('-')
    for i in range(int(seq[0]), int(seq[1]) +1):
        order_id = str(i)
        mid = len(str(order_id)) // 2
        firsthalf = order_id[:mid]
        secondhalf = order_id[mid:]
        if firsthalf == secondhalf:
            #print(f"{order_id} is corrupted")
            l.append(i)
print(f"The sum of the corrupt orders: {sum(l)}")
