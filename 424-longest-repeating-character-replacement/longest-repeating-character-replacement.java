class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character,Integer> count = new HashMap<>();
        int res=0;
        int l=0;
        int maxf=0;

        for(int r=0;r<s.length();r++){
            char rightch = s.charAt(r);
            count.put(rightch,count.getOrDefault(rightch,0)+1);

            maxf=Math.max(maxf,count.get(rightch));

            while((r-l+1) - maxf > k){
                char leftch = s.charAt(l);
                count.put(leftch,count.get(leftch)-1);
                l++;
            }
            res=Math.max(res,r-l+1);
        }
        return res;
    }
}