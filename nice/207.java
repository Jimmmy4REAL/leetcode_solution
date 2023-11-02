class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // constructing 2D dynamic array
        List<List<Integer>> adj = new ArrayList<>();
        for (int i=0;i<numCourses;i++){
            adj.add(new ArrayList<>());
        }
// row - a || col - b >> require take b first
        for (int i=0;i<prerequisites.length;i++){
            adj.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }
        // using int instead of hashset checking - > all init as 0
        int[] visit = new int[numCourses];
        // how to proper print out {0,0,0,0,0}
        System.out.println(visit);

        for (int i=0;i<numCourses;i++){
            if (visit[i]==0){
                if(helper(adj,visit,i)){
                    return false;
                }
            }
        }
        return true;
    }
    private boolean helper(List<List<Integer>> adj, int[] visit,int curr){
        if (visit[curr] == 2){
            return true;
        }
        visit[curr] = 2;
        for (int i=0;i<adj.get(curr).size();i++){
            if (visit[adj.get(curr).get(i)] != 1){
                // find cycle here
                if (helper(adj,visit,adj.get(curr).get(i))){
                    return true;
                }
            }
        }
            visit[curr] = 1; // why should be 1 cannot 0 - here using another string meaning remove from hashSet
            return false;
    }
}