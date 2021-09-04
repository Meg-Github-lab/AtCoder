l,q = map(int, input().split())
cx = [map(int, input().split()) for _ in range(q)]
c, x = [list(i) for i in zip(*cx)]
cnt=0
tumber = [0]*l
for i in range(q):
    if c[i] == 2:
        for k in tumber:
            if tumber[x[i]+cnt] == 0:
                cnt+=1
        print(tumber.count)