b = input()

base = [["A", "T"], ["C", "G"]]

for pair in base:
    if b in pair:
        pair.remove(b)
        print(pair[0])
        pair.append(b)
        break
