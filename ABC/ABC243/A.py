V, A, B, C = map(int, input().split())

remain = V

while True:
    remain -= A
    if remain < 0:
        print("F")
        break
    remain -= B
    if remain < 0:
        print("M")
        break
    remain -= C
    if remain < 0:
        print("T")
        break