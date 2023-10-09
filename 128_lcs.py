class Solution(object):
    def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = set()
        for elem in nums:
            record.add(elem)
        res,curr = 1,1
        for elem in record:
            if elem - 1 not in record:
                while elem + 1 in record:
                    elem += 1
                    curr += 1
                res = max(curr,res)
                # update curr_val to initial
                curr = 1
            
        return res
nums = [100,4,200,1,3,2]
print(Solution.longestConsecutive(nums)) # 4