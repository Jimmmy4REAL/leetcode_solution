class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # using adjacent list to represent graph
        # format of hashmap not 2Darray [too tricky]

        # hashset to record visit_path

        record = set()
        graph = {idx:[] for idx in range(numCourses)}
        for curr,pre in prerequisites:
            graph[curr].append(pre)
        # start traverse

        def helper(node):
            # deep into graph[curr]
            if node in record:
                return False
            if graph[node] == []:
                return True
            # continue recursion
            record.add(node)
            for nei in graph[node]:
                if helper(nei) is False:
                    return False
            record.remove(node)
            graph[node] = []
            return True
        
        for curr in range(numCourses):
            if helper(curr) is False:
                return False
        return True
