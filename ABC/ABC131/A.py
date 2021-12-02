S = input()

for index in range(3):
    if S[index] == S[index + 1]:
        print("Bad")
        exit()

print("Good")