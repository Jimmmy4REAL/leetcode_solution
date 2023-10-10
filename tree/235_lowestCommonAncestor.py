# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr =  curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr
        """
        # use feature of BST
        # relation of root p q
        if root.val == p.val or root.val == q.val:
            return root
        if p.val > q.val:
            p,q = q,p # always p is the smaller_one
        while True: # make sure that exist
            # traverse to find val that p < q
            if p.val <= root.val and root.val <= q.val:
                return root
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                root = root.left