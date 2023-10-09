class Solution(object):
    def isPalindrome(s):
        """

edge case consider >> line 19 and 21 IS l < r not relation with 0 OR len(s)

        :type s: str
        :rtype: bool
        """
        # change to lowerCase and remove all non-alphanumeric
        # check the same or not

        def helper(char):
            # if char belong to alphaNumeric
            return ord('0') <= ord(char) <= ord('9') or ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z')
        l,r = 0,len(s) - 1
        while l < r:
            # compare the valid_left and valid_right
            while l < r and not helper(s[l]):
                l += 1
            while l < r and not helper(s[r]):
                r -= 1
            # start comparing the two
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
s = "A man, a plan, a canal: Panama"
print(Solution.isPalindrome(s))