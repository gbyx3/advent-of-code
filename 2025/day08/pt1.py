import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Power of two a ** 2
# Square root: a ** 0.5

input_file = sys.argv[1]
input = open(input_file, "r")
lines = input.read().split()

res = {}
l = [ x for x in lines ]
boxes = [ x.split(",") for x in l]
for i, p in enumerate(boxes):
    for q in boxes[i+1:]:
        dist = 0
        for j in range(3):
            dist += (int(p[j]) - int(q[j])) ** 2
        dist = dist ** 0.5
        print(f"{dist} - Between {p} and {q}")


