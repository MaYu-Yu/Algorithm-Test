def subSet(atom, sub, i, n):
    if i > n:
        print(sub)
    else:
        subSet(atom, sub, i + 1, n)
        sub.append(atom[i])
        subSet(atom, sub, i + 1, n)
        sub.pop()
if __name__ == "__main__":
    atom = ['a','b','c','d']
    subSet(atom , [], 0, len(atom) - 1)