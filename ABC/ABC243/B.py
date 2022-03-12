import itertools

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

N_list = list(range(N))
same_num_idx = 0
same_num = 0

for num in range(N):
    if A_list[num] == B_list[num]:
        same_num_idx += 1

for idx_comb in itertools.permutations(N_list, 2):
    if A_list[idx_comb[0]] == B_list[idx_comb[1]]:
        same_num += 1

print(same_num_idx)
print(same_num)