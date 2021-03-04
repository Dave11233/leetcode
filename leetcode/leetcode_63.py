class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1:return 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        if i == 0 and j >= 1:
                            dp[i][j] = dp[i][j-1]
                        elif j == 0 and i >= 1:
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]



if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles(
        # [[0,0,0],[0,1,0],[0,0,0]]
        [[0,0],[1,1],[0,0]]
        )
    )