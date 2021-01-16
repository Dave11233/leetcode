class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        ans = []
        visited = [[False] * n for _ in range(n)]
        from collections import deque
        def dfs(path=[], start_node=0):
            if start_node == n - 1:
                ans.append(path+[start_node])
                return
            d = deque(graph[start_node])
            path.append(start_node)
            while d:
                next_node = d.popleft()
                if not visited[start_node][next_node]:
                    visited[start_node][next_node] = True
                    dfs(path, next_node)
                    visited[start_node][next_node] = False
            path.pop()

        dfs()
        return ans


if __name__ == '__main__':
    print(Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
