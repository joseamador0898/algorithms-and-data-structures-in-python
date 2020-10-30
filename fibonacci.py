#This solution is an iterative bottom-up approach with memoization to calculate the fibonacci number of N
class Solution:
    def fib(self, N: int) -> int:
        cache = {0: 0, 1: 1}
        
        if N <= 1:
            return N
        
        for i in range(2 , N + 1):
            cache[i] = cache[i-1] + cache [i-2]
            
        return cache[N]
#Can improve by further optimizing memory and/or further using mathematical equations to calculate fibonacci


        
        