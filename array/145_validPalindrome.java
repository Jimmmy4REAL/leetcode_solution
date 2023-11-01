class Solution{
    public boolean isPalindrome (String str){
        // check valid - then compare the left and right pointer
        // powerful internal built-in
        int l = 0;
        int r = str.length() - 1;

        // move two pointer
        while (l < r){
            Character start = str.charAt(l);
            Character end = str.charAt(r);
            if (!Character.isLetterOrDigit(start)){
                l++;
                continue;
            }
            if (!Character.isLetterOrDigit(end)){
                r--;
                continue;
            }
            // compare the two
            if (!((Character.toLowerCase(start)) == Character.toLowerCase(end))){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}