import numpy as np

N = int(input())
S_reel = [input() for _ in range(N)]
reel_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

cnt_list = []
for i in range(10):
    cnt = 0
    num_np = np.zeros(10)
    
    for k in range(N):
        num_np[S_reel[k].find(reel_num[i])] += 1
        
    for k in range(10):
        if num_np[9 - k] > 0:
            cnt += (9 - k) + (num_np[9 - k] - 1) * 10
            num_np = num_np - num_np[9 - k]

    cnt_list.append(cnt)

print(int(min(cnt_list)))
