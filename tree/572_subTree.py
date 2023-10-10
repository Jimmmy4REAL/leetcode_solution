# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def helper(one,two):
            if not one and not two:
                return True
            if not one or not two:
                return False
            if one.val != two.val:
                return False
            #one and two both has equal value -> further checked required
            return helper(one.left,two.left) and helper(one.right,two.right)
        

        # not binary search tree - more trivial
        if not root or not subRoot: # not equal
            return False
        if helper(root,subRoot): # reason that require manual checking here
            return True
        # the two not equal - > further traverse in root
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)