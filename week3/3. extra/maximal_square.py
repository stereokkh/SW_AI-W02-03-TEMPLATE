class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        area = 0
        dp = [[0 for _ in range(col+1)]for _ in range(row+1)]
        for r in range(1, row+1):
            for c in range(1, col+1):
                if matrix[r-1][c-1] == "1":
                    dp[r][c] = min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c]) + 1
                    area = max(area, dp[r][c])
        return area*area


                
                    


        