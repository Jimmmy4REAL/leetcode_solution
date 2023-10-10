# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # review different traversal
        # inorder \ preorder \ postOrder
        # find from inOrder index to separate left_subtree and right_subtree
        if preorder == [] and inorder == []:
            return None
        rootval = preorder[0]
        root = TreeNode(rootval)
        for idx in range(len(inorder)):
            if inorder[idx] == rootval:
                break # idx is determined as segment
        # left >> 0 to idx || right >> idx + 1 to end
        root.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        
        return root