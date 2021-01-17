
class Solution:
    """
    1st Solution: Naive approach
    Use two loops to iterate through the array and calculate all pair-sums, 
    then see if any of the pair-sums is equal to the target sum

    """
    def twoSumN(self, nums: List[int], target: int) -> List[int]:
         for i in range(len(nums) - 1):
             firstNum = nums[i]
             for  j in range(i+1, len(nums)):
                 secondNum = nums[j]
                 if firstNum + secondNum == target:
                     return[i, j]

class Solution:
    """
    2nd Solution: Optimal approach with hash table (=> python dictionary)
    Iterate ONCE through the nums array, and calculate the targetNumber,
    i.e. targetNum = target - num, then check if its in the dictionary, if it is
    then return the indices, and if not then append num into the dictionary

    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for idx,num in enumerate(nums):
            targetNum = target - num
            if targetNum in numsDict:
                return [idx, numsDict[targetNum]]
            else:
                numsDict[num] = idx


 

        