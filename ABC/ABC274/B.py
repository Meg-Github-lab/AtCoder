import numpy as np

H, W = map(int, input().split())
c_list = [list(input()) for _ in range(H)]
c_ndarray = np.array(c_list)

print(*list(np.count_nonzero(c_ndarray == "#", axis=0)))
