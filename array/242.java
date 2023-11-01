class Solution {
    public boolean isAnagram(String s, String t) {
        if (!(s.length() == t.length())){
            return false;
        }
        int[] record = new int[26];
        for (int i = 0; i < s.length();i ++){
            record[s.charAt(i) - 'a']++;
            record[t.charAt(i) - 'a']--;
        }
        for (int n:record){
            if (n != 0){
                return false;
            }
        }
        return true;
    }
}


    //     // check hashMap if are the same
    //     Map<Character,Integer> record1 = new HashMap<>();
    //     Map<Character,Integer> record2 = new HashMap<>();
    //     // traverse for count
    //     for (int i = 0;i < s.length(); i++){
    //         char chars = s.charAt(i);
    //         char chart = t.charAt(i);
        
    //     record1.put(chars,record1.getOrDefault(chars,0) + 1);
    //     record2.put(chart,record2.getOrDefault(chart,0) + 1);
    //     }
    //     return record1.equals(record2);
    // }}
    //     for (char elem:record1.keySet()){
    //         int val1 = record1.get(elem);
    //         int val2 = record2.getOrDefault(elem,0);
    //         if (!(val1 == val2)){
    //             return false;
    //         }
    //     }
    //     return true;
    // }
