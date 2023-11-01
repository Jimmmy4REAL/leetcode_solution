import java.io.*;

// if in one file format
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] arr = {1, 2, 3};
        return twoSumHidden(arr, 5);
    }
    public int[] twoSumHidden(int[] nums, int target) {
        Map<Integer,Integer> record = new HashMap<>();
        // loop through hashmap
        for (int i=0;i<nums.length;i++){
            int elem = nums[i];
            if (record.containsKey(elem)){
                return new int[]{i,record.get(elem)}; // return require array
            }
            record.put(target-nums[i],i);
        }    
        return new int[]{};
    }
}
// class Main{
// // input >> nums = [2,7,11,15], target = 9
// // Output: [0,1]
// // println(Solution.twoSum(input,target))
// }