import sys
input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split()
ranges = [x for x in lines if "-" in x]
ingredients = [x for x in lines if "-" not in x]
fresh = set()
for i in ingredients:
    for r in ranges:
        low, high = r.split("-")
        if int(low) <= int(i) <= int(high):
            print(f"{i} is fresh in range {r}")
            fresh.add(i)
print(f"Number of fresh ingredients: {len(fresh)}")

