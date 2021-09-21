# 解説の考え方
'''
問題文を
「長さが1の棒がN1個、長さが2の棒がN2個、長さが3の棒がN3個ある。長さがちょうど 5 に等しい棒を最大でいくつ作ることができるかを求めよ。」
という問題に言い換えて解く。

'''
# 参考コード（→https://atcoder.jp/contests/arc126/submissions/25851925）
def solve(n2, n3, n4):
    n1, n2, n3 = n2, n4, n3//2
    ans = 0

    comb = [(0, 1, 1), (2, 0, 1), (1, 2, 0), (3, 1, 0), (5, 0, 0)]  #(長さ1の棒の数、長さ2の棒の数、長さ3の棒の数)の組み合わせリスト。解説の「貪欲アルゴリズム」の順に並んでいる。
    for a, b, c in comb:
        k = n1 + n2 + n3
        if a > 0:
            k = min(k, n1//a)
        if b > 0:
            k = min(k, n2//b)
        if c > 0:
            k = min(k, n3//c)
        ans += k
        n1 -= a * k
        n2 -= b * k
        n3 -= c * k

    print(ans)

T = int(input())
for _ in range(T):
    solve(*map(int, input().split()))