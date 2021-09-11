import itertools
import collections

n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

for v in itertools.combinations(x,4):
    if len(collections.Counter(list(v))) == 2:
        print('Yes')

for v in itertools.combinations(y,4):
    if len(collections.Counter(list(v))) == 2:
        print('Yes')
