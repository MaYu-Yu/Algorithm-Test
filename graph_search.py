class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self, item): 
        self.q.insert(0,item)
    def dequeue(self):     
        return self.q.pop()
    def isEmpty(self):
        return self.getSize() == 0
    def getSize(self):
        return len(self.q)
def DFS(graph, start):
    visit = [False] * (len(graph) + 1)
    def dfs(graph, visit, start):
        visit[start] = True
        print(start, end = " ")
        for val in graph[start]:
            if not visit[val]: dfs(graph, visit, val)  
    print("DFS: ", end='')
    dfs(graph, visit, start)
    print()
def BFS(graph, start):
    print("BFS: ", end='')
    visit = [False] * (len(graph) + 1)
    visit[start] = True
    q = Queue()
    q.enqueue(start)
    while(not q.isEmpty()):
        v = q.dequeue()
        print(v, end = " ")
        for son in graph[v]:
            if not visit[son]:
                q.enqueue(son)
                visit[son] = True
    print()
# 找出每個連通單元
def hasCycle(graph):
    print("---連通單元---")
    visit = [False] * (len(graph) + 1)
    def dfs(graph, visit, u, v):
        visit[v] = True
        for n in graph:
            if u == n: break
            if visit[n]:
                pass #cycle = True
            else:
                dfs(graph, visit, v, n)
    for i in graph:
        if not visit[i]:
            dfs(graph, visit, i,i)
if __name__ == "__main__":
    graph = {
        1:[2,3],
        2:[1,4,5],
        3:[1,6,7],
        4:[2,8],
        5:[2,8],
        6:[3,8],
        7:[3,8],
        8:[4,5,6,7]
    }

    DFS(graph, 1)
    BFS(graph, 1)
    hasCycle(graph)