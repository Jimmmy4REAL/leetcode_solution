# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self,root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # iteration \ recursion
        if not root:
            return
        # start reverse
        root.left,root.right = root.right,root.left
        # recursive
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root