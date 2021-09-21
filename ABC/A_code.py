# 実行時間が最小の考え方
'''
解説記事（→https://atcoder.jp/contests/arc126/editorial/2623）の考え方を全てif~else文で記述したコード。
for文の使用回数が1回のみなので、実行時間が短いと思われる。しかし、コードのフレキシブル性はゼロかつコメントアウトがないと読みづらいので、良質なコードとは言い難い。
'''
# 参考コード（→https://atcoder.jp/contests/arc126/submissions/25990801）

T = int(input())

for _ in range(T):
    ans = 0
    N2, N3, N4 = map(int, input().split())
    N6 = N3 // 2    # N3は必ず2本ずつでしか長さ10の棒を作れないので、以後N6として考える。
    if N6 <= N4:    # (N2, N3, N4)=(0, 2, 1)の組み合わせが成立し、N3を最初に使い切る場合。
        ans += N6   # N6の個数だけ長さ10の棒ができる。
        N4 -= N6    # N6の個数だけN4の数が減る。
        N8 = N4 // 2    # N2, N4のみの時、N4は2組でしか消費できないのでひとつのかたまりN8として考える。
        
        if N2 >= N8:    # (N2, N3, N4)=(1, 0, 2)の組み合わせが成立し、N4を次に使い切る場合。
            ans += N8   # N8の個数だけ長さ10の棒ができる。
            N2 -= N8    # N8の個数だけN2の数が減る。
            N4 = N4 % 2     # N4の残りを考える。
            
            if N4 == 0:     # ピッタリN4を消費できた場合、すなわちN2のみ残っている場合。
                ans += N2 // 5  # N2 * 5 = 10なので、N2を5で割った時の商だけ長さ10の棒ができる。
            
            else:   # N4 = 1の時、すなわち (N2, N3, N4)=(x本, 0, 1)のとき。
                
                if N2 >= 3:     # (N2, N3, N4)=(3, 0, 1)の組み合わせが成立し、N4を使い切る場合。
                    ans += 1    # N4 = 1なので、長さ10の棒は1本のみできる。
                    N2 -= 3     # 消費した3本分だけ減る。
                    ans += N2 // 5   # N2 * 5 = 10なので、N2を5で割った時の商だけ長さ10の棒ができる。
        
        else:   # N2 < N8の時、すなわち(N2, N3, N4)=(1, 0, 2)の組み合わせが成立し、N2を使い切る場合。
            ans += N2   # N2の個数だけ長さ10の棒ができる。残りは(N2, N3, N4)=(0, 0, x本)となり、N4のみでは長さ10の棒を作れないので計算終了。
    
    else:   # N6 > N4の時、すなわち(N2, N3, N4)=(0, 2, 1)の組み合わせが成立し、N4を最初に使い切る場合。
        ans += N4   # N4の個数だけ長さ10の棒ができる。
        N6 -= N4    # N4の個数だけN6の数が減る。
        N4_2 = N2 // 2    # N2, N6のみの時、N4は2組でしか消費できないので、これらを一つのかたまりN4として考える。

        if N6 < N4_2:    # (N2, N3, N4)=(2, 2, 0)の組み合わせが成立し、N3を使い切る場合。
            ans += N6   # N6の個数だけ長さ10の棒ができる。
            N2 -= N6 * 2    # N6一つにつきN2は2つ消費するので、N6 * 2だけ減る。
            ans += N2 // 5  # N2 * 5 = 10なので、N2を5で割った時の商だけ長さ10の棒ができる。

        else:   # (N2, N3, N4)=(2, 2, 0)の組み合わせが成立し、N2を使い切る場合。
            ans += N4_2   # N4の個数だけ長さ10の棒ができる。残りは(N2, N3, N4)=(0, x本, 0)となり、N6のみでは長さ10の棒を作れないので計算終了。

    print(ans)