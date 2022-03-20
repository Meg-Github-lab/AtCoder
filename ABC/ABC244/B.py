N = int(input())
T = input()

x, y = 0, 0
rotate = 0

for num in range(N):
    if T[num] == "R":
        rotate += 1
        continue
    elif T[num] == "S":
        if rotate % 4 == 0:
            x += 1
        elif rotate % 4 == 1:
            y -= 1
        elif rotate % 4 == 2:
            x -= 1
        elif rotate % 4 == 3:
            y += 1

print(x, y, sep=" ")