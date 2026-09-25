#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)

        if n == 0:
            return 0

        # Initialize dp with the last row of the triangle.
        # This array will store the minimum path sum from the current level down to the bottom.
        # Its size is n, corresponding to the maximum length of a row (the last row).
        dp = list(triangle[n - 1])

        # Iterate from the second-to-last row up to the top row
        for i in range(n - 2, -1, -1):
            # Iterate through each element in the current row 'i'
            # The length of triangle[i] is i + 1
            for j in range(len(triangle[i])):
                # For each element triangle[i][j], the minimum path sum starting from it
                # is its value plus the minimum of the two adjacent elements in the row below.
                # dp[j] and dp[j+1] currently hold the minimum path sums from the (i+1)-th row.
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        # After processing all rows, dp[0] will contain the minimum path sum
        # starting from triangle[0][0] to the bottom.
        return dp[0]
# @lc code=end
