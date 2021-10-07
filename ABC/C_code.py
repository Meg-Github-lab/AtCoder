from itertools import permutations


N = list(input())


def list_difference(list1, list2):
    result = list1.copy()
    for value in list2:
        if value in result:
            result.remove(value)

    return result

ans = 0

for i in range(len(N)//2):

    for j in permutations(N, i+1):
        if j[0] == '0':
            continue

        A = int(''.join(j))
        B_list = list_difference(N, j)

        for k in permutations(B_list):
            if k[0] == '0':
                continue

            B = int(''.join(k))
            ans = max(ans, A*B)

print(ans)