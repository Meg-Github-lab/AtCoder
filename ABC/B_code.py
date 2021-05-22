s = input()

s_replace = s.translate(str.maketrans({'6': '9', '9': '6'}))
s_reverse = s_replace[::-1]

print(s_reverse)

# https://techacademy.jp/magazine/19188