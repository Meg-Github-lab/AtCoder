x = input()
n = int(input())
name_list = [input() for _ in range(n)]

my_dict = {x[i]: str(i) for i in range(26)}
my_table = str.maketrans(my_dict)

trans_list=[]
for i in range(n):
    s = []
    for j in name_list[i]:
        s.append(int(j.translate(my_table)))
    trans_list.append(s)

add_dict = dict(zip(name_list, trans_list))
dict_sorted = dict(sorted(add_dict.items(), key=lambda x: x[1]))
for key in dict_sorted.keys():
    print(key)