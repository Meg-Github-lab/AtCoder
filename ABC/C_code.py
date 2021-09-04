n =int(input())
q_list = [0]*n

p_list = list(map(int, input().split()))

for i in range(n):
    q_list[p_list[i]-1] = i+1

print(*q_list) 
