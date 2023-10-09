class Solution(object):
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        # using a sliding window to record - start from righter pointer
        record = set()
        res = 0
        l = 0
        for r in range(len(s)):
            # two route - add elem into set OR remove the duplicate + check target_updated                
            while s[r] in record:
                record.remove(s[l])
                l += 1
            record.add(s[r])
            res = max(res,r - l + 1) # notice when to update like here - not to update in advance
        return res

s = "a"
print(Solution.lengthOfLongestSubstring(s))