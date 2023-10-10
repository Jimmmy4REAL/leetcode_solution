class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # can flow from cell (ri, ci) to BOTH the Pacific and Atlantic oceans
        # if r,c in pac and r,c in atl >> append into the result_list

        # helper function design
        
        pac,atl = set(),set()
        rows,cols = len(heights),len(heights[0])
        directions = [[0,-1],[0,1],[1,0],[-1,0]]

        def helper(r,c,prev,record):
            if not (0<=r<rows and 0<=c<cols and (r,c) not in record and heights[r][c] >= prev):
                return # only to update hashset
            # update hashset
            record.add((r,c))
            # traverse different part
            for ar,ac in directions:
                helper(r+ar,c+ac,heights[r][c],record)
            return
        # update in atl and pac
        for r in range(rows):
            helper(r,0,0,pac)
            helper(r,cols - 1,0,atl)
        for c in range(cols):
            helper(0,c,0,pac)
            helper(rows-1,c,0,atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res