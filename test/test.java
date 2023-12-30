package test;


class Solution{
    public int maxLoss(int[] nums){
        // init var
        int currMax = nums[0];
        int res = 0;
        // traverse - > 1. calc res 2. update currMax
        for (int num:nums){
            res = Math.min(num - currMax, res);
            currMax = Math.max(currMax, num);
        }
        return res;
    }

    public static void main(String[] args){ // need to be in test.java so to exec
        int[] nums = {1,3,5,3,1,4};
        Solution solution = new Solution();
        int res = solution.maxLoss(nums);
        System.out.println(res);
    }
}

