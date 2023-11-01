class Solution {
    public int characterReplacement(String s, int k) {
        // check how many can be substitute - len(curr) - record.maxVal
        Map<Character,Integer> record = new HashMap<>();
        int l = 0;
        int res = 0;
        for (int r = 0;r < s.length();r++){
            char elem = s.charAt(r);
            record.put(elem,record.getOrDefault(elem,0) + 1);

        if (r-l+1-Collections.max(record.values()) > k){
            // update require
            char lStr = s.charAt(l);
            record.put(lStr, record.get(lStr) - 1);
            l++;
        }
        res = Math.max(r-l+1,res);
    }
    return res;
}
}