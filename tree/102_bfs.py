# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # pop_left >> queue
        if not root:
            return []
        q = [root]
        res = []
        while q:
            curr = [] # final step is to q.append(curr)
            for _ in range(len(q)):
                node = q.pop(0)
                # logic >> node.val to curr_array AND insert new node into q
                curr.append(node.val)
                # potential left and right node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr)
        return res