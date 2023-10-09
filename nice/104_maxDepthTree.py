# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
================================================
        if not root:
            return 0
        # finally return back to init stage
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        if not root:
            return 0
        q = [root]
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1
        return res
=======================================================
        # iteration stack
        if not root:
            return 0
        
        stack = [[root,0]]
        res = 0
        # similar with diameter of tree
        # return back 1 + max(node.left >> depth, node.right >> depth)
        while stack:
            node,depth = stack.pop()
            res = max(res,depth)
            if node:
                stack.append([node.left,depth + 1])
                stack.append([node.right,depth + 1])
        return res
        """
        if not root:
            return 0
        
        stack = [[root,0]]
        res = 0
        while stack:
            node,depth = stack.pop()
            res = max(res,depth)
            if node:
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res