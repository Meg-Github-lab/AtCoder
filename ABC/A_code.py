# 最短コード長の考え方
'''
print((N2*2+min(N3*2,N2+N4*2)*3+min(N4,N2*2+N3)*4)//10)の考え方がいまいちわからない。
レッドコーダーの人は別世界の人だなと感じた。
'''
# 参考コード（→https://atcoder.jp/contests/arc126/submissions/25997402）

for _ in "_"*int(input()):N2, N3, N4 = map(int, input().split()) ;N3 //= 2;print((N2*2+min(N3*2,N2+N4*2)*3+min(N4,N2*2+N3)*4)//10)

'''
Pythonでの;(セミコロン)は区切り文字として使える。
参考にしたサイト
https://www.javadrive.jp/python/ini/index3.html#:~:text=Python%20%E3%81%A7%E3%81%AF%E3%82%BB%E3%83%9F%E3%82%B3%E3%83%AD%E3%83%B3(%3B)%E3%82%82,%E3%82%BB%E3%83%9F%E3%82%B3%E3%83%AD%E3%83%B3%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%BE%E3%81%99%E3%80%82

'''