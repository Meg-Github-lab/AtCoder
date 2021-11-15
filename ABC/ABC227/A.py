N, K, A = map(int, input().split())

last = A + K - 1
last %= N
if last == 0:
    last = N

print(last)