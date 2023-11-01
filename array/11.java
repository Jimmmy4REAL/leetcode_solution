package array;

public class Solution {
    public int maxArea(int[] height) {
        // two pointer to check
        int l = 0;
        int r = height.length - 1;
        int res = 0;
        while (l < r){
            // calc curr and judge move l OR r pointer
            int rval = height[r];
            int lval = height[l];
            int curr = Math.min(rval,lval) * (r-l);
            res = Math.max(curr,res);
            if (rval > lval){
                // move l pointer
                l++;
            }
            else{
                r--;
            }
        }
        return res;
    }
}