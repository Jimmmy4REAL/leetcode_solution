package test;


import java.util.HashSet;
import java.util.Set;

class Solution{
    
    public boolean containsDuplicate (int[] nums) {
        Set<Integer> record = new HashSet<>();
        for (int i=0;i<nums.length;i++){
            // two path
            if (record.contains(nums[i])){
                return true;
            }
            // update into hashSet
            record.add(nums[i]);
        }
        return false;
    }
    public static void main(String args[]){
        int[] nums = {1,1,2};
        Solution solution = new Solution(); // Create an instance of the Solution class
        boolean output = solution.containsDuplicate(nums); // Call the method on the instance
        System.out.println(output);
    }
}