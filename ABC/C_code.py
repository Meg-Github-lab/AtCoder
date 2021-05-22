n = int(input())
a = []
b = []
c = []
num_list = []
for i in range(3):
    num_list.append(list(map(int,input().split())))
a = num_list[0]
b = num_list[1]
c = num_list[2]
cnt = 0
#print(a,b,c)

for i in a:
    for j in c:
        if j <= n:
            if i ==b[j-1]:
                cnt += 1

print(cnt)

# https://qiita.com/ell/items/1f519aff0cdc3cf16284
