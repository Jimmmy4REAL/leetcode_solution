import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        // can return in any order
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        helper(res,0,nums,list);
        return res;
    }
    // many input
    public void helper(List<List<Integer>> ans,int start, int[] nums,List<Integer> list
    ){
        if (start >= nums.length){
            ans.add(new ArrayList<>(list)); // update in ans output_array
        }
        else{
        list.add(nums[start]);
        helper(ans,start+1,nums,list);

        // pop out here
        list.remove(list.size()-1);
        helper(ans,start+1,nums,list);
        }
    }
}