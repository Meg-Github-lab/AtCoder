p = map(int, input().split())
alpha = ''

num2alpha = lambda c: chr(c+96)
for num in p:
    alpha = alpha+ num2alpha(num)

print(alpha)