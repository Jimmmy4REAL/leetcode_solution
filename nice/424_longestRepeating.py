import collections
class Solution(object):
    def characterReplacement(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # can modify k times
        # ABAB 2 > 4
        # AABAABA 1 > 4
        # continue from the different elem - sliding window for + while
        res = 0
        record = collections.defaultdict(int)
        l = 0
        for r in range(len(s)):
            # two routes
            # update counter and continue OR to remove one left_pointer element
            record[s[r]] += 1
            
            if r - l + 1- max(record.values()) > k:
                record[s[l]] -= 1
                l += 1
            res = max(r-l + 1,res)

        return res

s = "BAAA"
k = 0
print(Solution.characterReplacement(s,k)) # expect to be 4