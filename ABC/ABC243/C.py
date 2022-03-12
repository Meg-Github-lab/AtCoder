import itertools
import sys

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
S = input()

indexes = [i for i, x in enumerate(y) if x == 1]
print(indexes) # [0, 2, 4]