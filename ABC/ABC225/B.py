N = int(input())


for i in range(N - 1):
    if i == 0:
        ans = set(map(int, input().split()))
        continue
    ab_i = set(map(int, input().split()))
    ans = ab_i & ans
    if len(ans) == 0:
        print("No")
        break

if len(ans) == 1:
    print("Yes")