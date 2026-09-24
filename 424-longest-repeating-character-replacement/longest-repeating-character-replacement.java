class Solution {
    public int characterReplacement(String s, int k) {
        HashMap <Character, Integer> count = new HashMap<>();
        int l=0;
        int maxFreq=0;
        int result=0;

        for(int r=0;r<s.length();r++){
            char rc=s.charAt(r);
            count.put(rc,count.getOrDefault(rc,0)+1);
            maxFreq=Math.max(maxFreq,count.get(s.charAt(r)));
            int replacements=(r-l+1)-maxFreq;
            if(replacements>k){
                char lc=s.charAt(l);
                count.put(lc,count.get(lc)-1);
                l++;
                replacements=(r-l+1)-maxFreq;
            }
            result=Math.max(result,r-l+1);
        }
        return result;
    }
}