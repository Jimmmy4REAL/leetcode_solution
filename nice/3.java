class Solution {
    public int lengthOfLongestSubstring(String s) {
        // hashset - > if found duplicate - > reduce till not anymore
        Set<Character> record = new HashSet<>();
        // two pointer require
        int l = 0;
        int res = 0;
        for (int r = 0;r<s.length();r++){
            // compare in the two
            char curr = s.charAt(r);
            while (record.contains(curr)){
                // require remove and update left pointer
                char removed = s.charAt(l);
                record.remove(removed);
                l += 1;
            }
            record.add(curr);
            res = Math.max(res,r-l+1);
        }
        return res;
    }
}