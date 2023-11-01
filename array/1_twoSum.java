package array;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
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
} {
    
}
