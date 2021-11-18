A, B = map(int, input().split())

ans = 0

for _ in range(2):
    ans += max(A, B)
    if ans == A:
        A -= 1
    elif ans == B:
        B -= 1

print(ans)