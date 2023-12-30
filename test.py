class Solution:
    def maxLoss(nums):
        res = 0
        currMax = nums[0]
        for elem in nums:
            res = min(res,elem - currMax)
            currMax = max(elem, currMax)

        return res
    
nums = [3,2,4,2,2,5]
print(Solution.maxLoss(nums)) # -2