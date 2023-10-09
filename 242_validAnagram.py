import collections
class Solution:
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        record_1 = collections.defaultdict(int) # 0
        record_2 = collections.defaultdict(int) # 0
        for idx in range(len(s)):
            record_1[s[idx]] += 1
            record_2[t[idx]] += 1
# {a:2,b:2} == {a:2,b:1}
        return record_1 == record_2
    
s = 'abfdsafas'
t = 'fdsafasd'
t_2 = 'abfdsafsa'

print(Solution.isAnagram(s,t)) # false 
print(Solution.isAnagram(s,t_2)) # true

