class Solution {
    public int numIslands(char[][] grid) {
        // dfs and bfs
        int count = 0;
        // extract 2D array length
        int rows = grid.length;
        int cols = grid[0].length;
        for (int r=0;r < rows;r++){
            for (int c = 0;c<cols;c++){
                if (grid[r][c] == '1'){
                    // call helper function
                    count++;
                    helper(r,c,rows,cols,grid);
                }
            }
        }
        return count;
    }
    // public void helper(int r,int c,int rows,int cols,char[][] grid){
    //     // edge case determine - separate condition
    //     if (!((0<=r && r<rows) && (0<=c && c<cols) && grid[r][c] == '1')){
    //         return;
    //     }
    //     // dfs traversing -- update to 3 first
    //     grid[r][c] = '0';
    //     // List<List<Integer>> NOTICE here - using int[][] here
    //     int[][] directions = {{0,-1},{0,1},{1,0},{-1,0}};
    //     for (int[] direction:directions){
    //         int updateR = direction[0]; // parse step by step
    //         int updateC = direction[1];
    //         // call four times
    //         helper(r+updateR,c+updateC,rows,cols,grid);
    //     }
    // }
    public void helper(int r,int c,int rows,int cols,char[][] grid){
        // bfs using queue
        Queue<List<Integer>> q = new LinkedList<>();
        q.add(Arrays.asList(r,c));
        // start for-loop and checking
        while (!q.isEmpty()){
            List<Integer> node = q.poll();
            int rcurr = node.get(0);
            int ccurr = node.get(1);
            if (!((0<=rcurr && rcurr<rows) && (0<=ccurr && ccurr<cols) && grid[rcurr][ccurr] == '1')){
             continue;
         }
            // update to '0' and put in neighbor into q
            grid[rcurr][ccurr] = '0';
            int[][] directions = {{0,-1},{0,1},{1,0},{-1,0}};
            for (int[] direction:directions){
                // append into q
                int updateR = direction[0]; // parse step by step
                int updateC = direction[1];
                q.add(Arrays.asList(rcurr+updateR,ccurr+updateC));
            }
        }
        return;
    }
}