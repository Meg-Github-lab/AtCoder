N = int(input())

num_set = set(range(1, 2*N+2))

for num in range(2*N + 1):
    print(list(num_set)[0])
    num_set.discard(list(num_set)[0])

    Aoki = int(input())
    if Aoki == 0:
        break
    num_set.discard(Aoki)