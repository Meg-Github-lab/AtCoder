A, B = input().split()

def sum_digit(num_str):
    digit = len(num_str)
    ans = 0

    for i in range(digit):
        ans += int(num_str[i])

    return ans

print(max(sum_digit(A), sum_digit(B)))