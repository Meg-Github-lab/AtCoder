X, Y = map(int, input().split())

diff = Y - X
if diff <= 0:
    print(0)
elif diff > 0:
    if diff % 10 != 0:
        ans = diff // 10 + 1
    elif diff % 10 == 0:
        ans = diff // 10
    print(ans)