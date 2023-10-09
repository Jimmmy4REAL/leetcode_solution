class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        # stack - close in same order
        stack = []
        record = {']':'[','}':'{',')':'('}
        # first in first out characteristic
        # check if insert elem belong to dictionary_key - > find in stack pop_val if the same
        # ]-[ >> return False or to continue traversing

        # okay to leave [ opened !!
        for elem in s:
            if elem in record:
                # check the pop out elem
                if stack and stack[-1] == record[elem]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(elem)
        return stack==[]
s = "()[]{}"
s2 = "("
print(Solution.isValid(s))
print(Solution.isValid(s2))