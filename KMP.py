def kmp(strs, pattern):
    perfix = [-1] * len(pattern) 
    i = -1
    for j in range(1, len(pattern)):
        while(i > -1 and pattern[i+1] != pattern[j]): 
            i = perfix[i] 
        if pattern[i+1] == pattern[j]:
            i+=1
            perfix[j] = i
    print("Perfix:", perfix)
    i = -1
    for j in range(len(strs)):
        while(i > -1 and pattern[i+1] != strs[j]):
            i = perfix[i]
        if pattern[i+1] == strs[j]: 
            i+=1
        if i == len(pattern) - 1: 
            return j - i
strs = "abcabcacab"
pattern = "cab"
print(kmp(strs, pattern))