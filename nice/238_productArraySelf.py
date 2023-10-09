class Solution:
    def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        >> Given an integer array nums, 
        return an array answer such that answer[i] is equal to 
        the product of all the elements of nums except nums[i].
        """
        # [1,2,3,4] = > [24,12,8,6]
    # pre  1,2,6,24  >> 1 1 2 6
    # suf 24,24,12,4
    #     24,12,8,6
        res = [1 for _ in range(len(nums))]
        pre =  1
        for idx in range(len(nums)):
            # prefix traverse
            res[idx] *= pre
            pre *= nums[idx]
        suf = 1
        for idx in range(len(nums) - 1,-1,-1):
            # reverse logic
            res[idx] *= suf
            suf *= nums[idx]
        return res
nums = [1,2,3,4] 
print(Solution.productExceptSelf(nums))