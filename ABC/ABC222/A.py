N = input()

print(N if len(N) == 4 else '0' * (4 - len(N)) + N)