class Solution {
    int res = 0;
    public int maxAreaOfIsland(int[][] grid) {
        for (int i = 0;i < grid.length; i++){
            for (int j=0;j< grid[0].length;j++){
                res = Math.max(res,helper(grid,i,j));
            }
        }
        return res;
    }

    public int helper(int[][] grid, int r,int c){
        if (r<0 || c<0 || r == grid.length || c== grid[0].length || grid[r][c] == 0){
            return 0;
        }
        grid[r][c] = 0;
        return (1 + helper(grid, r + 1, c) +
                helper(grid, r - 1, c) +
                helper(grid, r, c + 1) +
                helper(grid, r, c - 1));
    }
}