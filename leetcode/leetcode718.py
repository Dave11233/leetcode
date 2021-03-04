class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        length_a = len(A)
        length_b = len(B)
        dp = [[0]*(length_a+1) for _ in range(length_b)]
        for i in range(length_a + 1):
            if A[i] == B[i]:
                dp[i][i] = 1
        for i in range(length_a + 1):
            if A[0] == B[i]:
                dp[0][i] = 1

        for i in range(1,length_b+1):
            for j in range(1, length_a + 1):
                if A[j] == B[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1

        return max(max(x) for x in dp)
