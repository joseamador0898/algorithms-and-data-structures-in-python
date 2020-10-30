#https://leetcode.com/problems/decode-ways/
#This solution uses a dynamic programming approach to solving the ways you can decode a string of digits
import sys
for line in sys.stdin:
  
    if not line:
        print(0) 
    
    dp = [0 for _ in range(len(line) + 1)]
    
    dp[0] = 1
    
    if line[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1
    
    for i in range(2, len(dp)):
        if line[i - 1] != '0':
            dp[i] += dp[i-1]
        two_digit = int(line[i-2: i])
        if two_digit >= 10 and two_digit <= 26:
            dp[i] += dp[i-2]
            
    print(dp[len(line)]) 