class Solution {
    public int maxVowels(String s, int k) {
        int count=0;
        int maxcount=0;
        String vowels = "aeiou";

        for(int i=0;i<s.length();i++){
            //add new char
            if(vowels.indexOf(s.charAt(i))!=-1){
                count++;
            }
            //remove char leaving window
            if(i>=k){
                if(vowels.indexOf(s.charAt(i-k))!=-1){
                    count--;
                }
            }
            maxcount=Math.max(maxcount,count);
        }
        return maxcount;
    }
}