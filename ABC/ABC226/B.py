N = int(input())

ans_list = [[] for _ in range(N)]


for i in range(N):
    if i == 0:
        cnt = 1
        a0_list = list(input().split())
        L0 = int(a0_list.pop(0))
        a0 = ''.join(a0_list)

        ans_list[L0-1].append(a0)
        
        continue

    a_list = list(input().split())
    L = int(a_list.pop(0))
    a = ''.join(a_list)
    

    if a in ans_list[L-1]:
        continue
    else:
        cnt += 1
        ans_list[L-1].append(a)
    

print(cnt)
