import sys

S = input()
T = input()

if S == T:
    print('Yes') 
    sys.exit()

no_match_list = []
for i in range(len(S)):
    if S[i] == T[i]:
        continue

    elif S[i] != T[i]:
        no_match_list.append(i)


if len(no_match_list) == 2 and S[no_match_list[0]] == T[no_match_list[1]] and S[no_match_list[1]] == T[no_match_list[0]] and no_match_list[1] - no_match_list[0] == 1:
    print('Yes')
else:
    print('No')
