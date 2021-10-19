import string

alpha_list = list(string.ascii_lowercase)

C = input()

print(alpha_list[alpha_list.index(C) + 1])