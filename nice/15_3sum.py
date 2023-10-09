class Solution:
    def threeSum(nums):
        # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
        # such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        # Notice that the solution set must not contain duplicate triplets
        res = []
        # one,two,three
        # [-1,0,1,2,-1,-4] >> 0
        # -4,-1,-1,0,1,2
        # -1,0,1 AND -1,-1,2
        nums.sort() # sort array
        for idx in range(len(nums) - 2):
            if idx >= 1 and nums[idx] == nums[idx-1]:
                # move pointer to avoid duplicate
                continue
            
            l,r = idx + 1,len(nums) - 1
            one = nums[idx]
            
            while l < r:
                if one + nums[l] + nums[r] == 0:
                    res.append([nums[idx],nums[l],nums[r]])
                    l += 1
                    # require move left pointer
                    while l < r and nums[l] == nums[l-1]: # need to change 
                        l += 1
                elif one + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return res
nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(nums))