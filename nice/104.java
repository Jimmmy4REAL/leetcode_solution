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
    public int maxDepth(TreeNode root) {

        // if (root == null){
        //     return 0;
        // }
        // return 1+Math.max(maxDepth(root.left),maxDepth(root.right));

// Two Java Iterative solution DFS and BFS

    // bfs - queue - init | poll | offer
    
    //     if (root == null){
    //         return 0;
    //     }
    //     Queue<TreeNode> q = new LinkedList<>();
    //     q.offer(root); // offer mean 'append'
    //     int count = 0;
    //     while (!q.isEmpty()){
    //         int size = q.size();
    //         while(size -- > 0){
    //             TreeNode node = q.poll();
    //             if(node.left != null) {
    //             q.offer(node.left);
    //             }
    //             if(node.right != null) {
    //                 q.offer(node.right); 
    //             }
    //     }
    //     count++;

        
    // }
    // return count;
    // dfs - stack
    if (root==null){
        return 0;
    }
    Stack<TreeNode> stack = new Stack<>();
    Stack<Integer> value = new Stack<>(); // corresponding val
    stack.push(root);
    value.push(1);
    int max = 0;
    while (!stack.isEmpty()){
        TreeNode node = stack.pop();
        int tmp = value.pop();
        max = Math.max(tmp,max);
        if (node.left!= null){
            stack.push(node.left);
            value.push(tmp + 1);
        }
        if (node.right!= null){
            stack.push(node.right);
            value.push(tmp + 1);
        }
    }
    return max;
    }
}