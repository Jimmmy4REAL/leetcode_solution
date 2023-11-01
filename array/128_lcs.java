class Solution{
    public int longestConsecutive (int[] nums){
        // use hashSet
        Set<Integer> record = new HashSet<>();
        for (int num:nums){
            record.add(num);
        }
        // traverse and compare with curr_max
        int res = 0;
        for (int i=0;i < nums.length;i++){
            int elem = nums[i];
            int curr = 1;
            if (!(record.contains(elem-1))){
                while (record.contains(elem+1)){
                // continue moving
                curr += 1;
                elem += 1;
            }
        }
        res = Math.max(res,curr);
    }
        return res;
    }
}