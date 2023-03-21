def permutation(element, first, last):
    if first == last - 1:
        for i in range(last): print(element[i], end=' ')
        print()
    else:
        for i in range(first, last):
            element[first], element[i] = element[i], element[first]
            permutation(element, first + 1, last)
            element[first], element[i] = element[i], element[first]
if __name__ == "__main__":
    # 任意排列 element
    element = ['a','b','c','d']
    permutation(element, 0, len(element))
