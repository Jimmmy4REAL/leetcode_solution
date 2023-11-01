package array;

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
}