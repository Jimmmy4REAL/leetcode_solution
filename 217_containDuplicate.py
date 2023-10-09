# Given an integer array nums, 
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# [2,3,4,5,2]
# set() - route - > 1. put 2 3 4 5 into set OR 2. check if duplicate

class Solution:
    def containDuplicate(nums):
        # input >> integer array
        # output >> boolean
        record = set()
        for elem in nums:
            # two routes
            if elem not in record:
                record.add(elem)
            else:
                return True
        return False
    
test_1 = [2,3,4,5,2] # true
test_2 = [2,3,4,5] # false 
print(Solution.containDuplicate(test_1))
print(Solution.containDuplicate(test_2))