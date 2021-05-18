# https://atcoder.jp/contests/abc003/tasks/abc003_1

n = int(input())
n_list = list(range(1,n+1))

print(int(1/n * sum(n_list) * 10000))