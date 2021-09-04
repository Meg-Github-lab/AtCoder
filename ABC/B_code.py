AtCoder_contest = ['ABC', 'ARC', 'AGC', 'AHC']

s_list = [input() for _ in range(3)]
ans = list(set(AtCoder_contest) - set(s_list))
print(ans[0])