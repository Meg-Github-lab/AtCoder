N, K = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

max_idx = [i+1 for i, v in enumerate(A_list) if v == max(A_list)]
hate = set(max_idx) & set(B_list)

if len(hate) != 0:
    print("Yes")
else:
    print("No")