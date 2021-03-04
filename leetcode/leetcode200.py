"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
"""


class Solution:
    def numIslands(self, grid) -> int:
        """
        从返回的答案看的话，进行深度优先遍历；
        岛屿的个数就是完全图的个数。
        """
        if not grid:
            return 0

        if len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        visitied = [[False] * n for _ in range(m)]

        def dfs(grid, x, y):
            if x < 0 or x >= m or y >= n or y < 0 or visitied[x][y] or grid[x][y] == "0":
                """
                边界条件，当访问位置不是岛屿或者处于边界之外的时候停止递归。
                """
                return
            if grid[x][y] == "1":
                visitied[x][y] = True
                dfs(grid, x - 1, y)  # 向上访问
                dfs(grid, x + 1, y)  # 向下访问
                dfs(grid, x, y - 1)  # 向左访问
                dfs(grid, x, y + 1)  # 向右访问

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visitied[i][j]:  # 找到未访问的岛屿
                    dfs(grid, i, j)  # 访问一个未访问的完整岛屿
                    ans += 1
        return ans
