N, X = map(int, input().split())
As = list(map(int, input().split()))

cnt = 0
knows = [False] * N

while not knows[X-1]:
    knows[X-1] = True
    X = As[X-1]
    cnt += 1

print(cnt)