class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 1 stand for land \ 0 stand for water
        # if already checked could potential use signal

# use as signal OR to use hashset for marker!!

        rows,cols = len(grid),len(grid[0])
        def helper(r,c):
            # mark as *
            directions = [[0,-1],[0,1],[1,0],[-1,0]]
            # not matter using q or stack - bfs \ dfs
            stack = [[r,c]]
            while stack:
                r,c = stack.pop()
                if not (0<=r<rows and 0 <= c < cols and grid[r][c] == '1'):
                    continue
                grid[r][c] = '*'
                for left,right in directions:
                    stack.append([left+r,right+c])
            return
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    helper(r,c)
                    res += 1
        return res