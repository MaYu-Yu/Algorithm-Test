class Max_heap:
    h = []
    n = -1
    def __init__(self, max_size):
        self.h = [None] * max_size
    def insert(self, val):
        self.n+=1
        i = self.n
        self.h[i] = val
        if i == 0: 
            return 
        while(i != 0):
            if self.h[i] > self.h[(i-1)//2]:
                self.h[i], self.h[(i-1)//2] = self.h[(i-1)//2], self.h[i]
                i//=2
            else:
                i = 0
    def heapify(self):
        if self.n < 1: return 
        i, j = 0, 1
        while(j <= self.n): 
            if j < self.n and self.h[j] < self.h[j + 1]: # 左右子樹誰大
                j+=1
            if self.h[i] < self.h[j]: 
                self.h[i], self.h[j] = self.h[j], self.h[i]
                i, j = j, 2*j + 1
            else:
                j = self.n + 1
# root為最大 把最後一個節點一到root
# 依序往下比較，且維持max_heap的特性
    def delete_max(self):
        if self.n == -1: return
        self.h[0] = self.h[self.n]
        self.n-=1
        self.heapify()
    def print(self):
        print("Max_heap:")
        for i in range(self.n + 1):
            print(self.h[i], end=' ')
        print()
if __name__ == "__main__":
    heap = Max_heap(10)
    for i in [46,15,37,12,8,24]:
        heap.insert(i)
    heap.print()
    heap.delete_max()
    heap.print()