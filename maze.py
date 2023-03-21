class Solution(object):
    def solevMaze(self, maze, m, n):
        def dfs():
            mark =0
        mark = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(n+1): 
            mark[0][i] = 1
            mark[i][0] = 1
        dfs(maze, mark)
        return maze    
if __name__ == "__main__":
    a = Solution()
    m, n = 7, 7
    maze = {{0, 0, 1, 1, 1, 1, 1}, 
        {1, 0, 0, 0, 0, 0, 1}, 
        {0, 0, 1, 0, 1, 0, 1}, 
        {1, 0, 0, 1, 0, 1, 1}, 
        {1, 1, 0, 1, 0, 1, 1}, 
        {0, 0, 0, 0, 0, 0, 1}, 
        {1, 0, 1, 0, 1, 0, 0}}
    print(a.solevMaze(maze, m, n))