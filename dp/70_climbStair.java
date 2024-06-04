class Solution {
    public int climbStairs(int n) {
        // init for loop
        // 1 2 3 5
        // start from 3 - > the sum of prev_two

        if (n == 1) return 1;
        if (n == 2) return 2;
        int a = 1;
        int b = 2;
        int res=0;
        for (int i=3;i<=n;i++){
            res = a + b;
            
            a = b;
            b = res;
        }
        return res;
    }
}