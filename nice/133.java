/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors; // notice here the difference
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
    implement as node - > all node construct as graph
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        Map<Node,Node> record = new HashMap<>(); // oldToNew mapping
        Node output = helper(node,record);
        return output;
    }
    public Node helper(Node node, Map<Node,Node> record){
        if (record.containsKey(node)){
            return record.get(node); // return newNode already constrcuted
        }
        if (node == null){
            return null;
        }
        // require construct new node
        Node newNode = new Node(node.val);
        record.put(node,newNode);
        // base on oldNode neighbor relation - recursive calling helper func
        for (Node nei:node.neighbors){
            newNode.neighbors.add(helper(nei,record));
        }
        return newNode;
    }
}