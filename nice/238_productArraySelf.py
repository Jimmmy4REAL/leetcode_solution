class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        >> Given an integer array nums, 
        return an array answer such that answer[i] is equal to 
        the product of all the elements of nums except nums[i].
        """
        # [1,2,3,4] = > [24,12,8,6]
        # [1,2,6,24]
        # [24,12,4,1] > 