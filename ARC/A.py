N = input()
d = len(N)
m = d - 1
ans = 0

for i in range(m):
    ans += (m-i) * (10 ** i)

for i in range(d):
    if N[0] == '0':
        pass

    else:
        if N[0] != '1':
            N = 2 * 10 ** (m-i) - 1
            
        N = int(N)
        ans += N - 10 ** (m-i) + 1
        N = str(N)[1:]

print(ans)