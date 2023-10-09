import heapq
import collections

class Solution:
    def topKFrequent(nums, k):
        # [1,1,1,2,2,3], k = 2 >> output [1,2]

        # heap
        # [1,2]
        record = collections.defaultdict(int) # += 1
        for elem in nums:
            record[elem] += 1
        

        heap = [(-val,key) for key,val in record.items()]
        heapq.heapify(heap) # [(-3,1),(-2,2),,(-1,3)]

        res = []
        while k > 0:
            k -= 1
            val = heapq.heappop(heap)[1]
            res.append(val)

        return res
    def topKFrequent_2(nums, k):
        # [1,1,1,2,2,3], k = 2 >> output [1,2]
        # [1,2]

        # bucket sort
        bucket = [[] for _ in range(len(nums) + 1)]
        record = collections.defaultdict(int) # += 1
        for elem in nums:
            record[elem] += 1
        # reduce k base on len_List
        for elem in record:
            # format of list
            bucket[record[elem]].append(elem)
        res = []
        for idx in range(len(nums),0,-1):# not include 0 >> stop when reach 1
            if bucket[idx]:
                for elem in bucket[idx]:
                    res.append(elem)
                k -= len(bucket[idx])
                if k == 0:
                    return res

            
nums = [1,1,1,2,2,3]
k = 2
print(Solution.topKFrequent_2(nums,k))