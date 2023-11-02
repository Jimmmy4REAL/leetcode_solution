/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // call isSameTree function to find one valid
        
        if (subRoot == null || isSameTree(root, subRoot)) return true;

        if (root == null){
            return false;
        }
        return isSubtree(root.left,subRoot) || isSubtree(root.right,subRoot);
        
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        // compare the two
        if (p == null && q == null){
            return true;
        } 
        else if (p != null && q!=null && p.val==q.val){
            // recursive calling
            return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
        }
        else{
            return false;
        }
    }
}