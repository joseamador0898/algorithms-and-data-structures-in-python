class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        #Initialize dp array
        dp = [0] * n

        #Base case n=1, only one way to get to step 1
        #0 -> 1
        dp[0] = 1

        #Base case n=2, two ways to get to step 2
        #0 -> 1 -> 2
        #0 -> 2
        dp[1] = 2

        #Bottom-up DP approach to calculate no. of ways for N steps
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n-1]
