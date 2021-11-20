S, T, X = map(int, input().split())

if S > T and S > X:
    T += 24
    X += 24
elif S > T and S <= X:
    T += 24

if S <= X < T:
    print("Yes")
else:
    print("No")