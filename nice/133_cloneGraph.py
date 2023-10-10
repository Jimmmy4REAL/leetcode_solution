
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # each node_val is unique
        # hashset to record node_object

        # recursion \ dfs \ bfs
        if not node:
            return
        # traverse and add
        record = {} # have to use hashmap - reduce time complexity
        def helper(node):
            if node in record:
                return record[node]
                # deep into the neightbor val -> curr = curr.neighbor
            copy = Node(node.val)
            record[node] = copy
            for elem in node.neighbors:
                copy.neighbors.append(helper(elem))
            return copy
        return helper(node)