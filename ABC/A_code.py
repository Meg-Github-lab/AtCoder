n = int(input())
for _ in range(n):
    n2, n3, n4 = map(int, input().split())
    cnt = 0
    n2_list = ['*']*n2
    n3_list = ['*']*n3
    n4_list = ['*']*n4

    if n3//2 <= n4:
        cnt += n3//2
        n4 -= n3//2
        
