class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1=s1.length();
        int n2=s2.length();
        if(n1>n2){
            return false;
        }
        int[] s1_counts = new int[26];
        int[] s2_counts = new int[26];

        //count characters in s1
        for(int i=0;i<n1;i++){
            s1_counts[s1.charAt(i)-'a']++;
            s2_counts[s2.charAt(i)-'a']++;
        } 
        //check first window
        if (Arrays.equals(s1_counts,s2_counts)){
            return true;
        }
        //slide the window
        for(int i=n1;i<n2;i++){
            s2_counts[s2.charAt(i)-'a']++;
            s2_counts[s2.charAt(i-n1)-'a']--;
            if(Arrays.equals(s1_counts,s2_counts)){
                return true;
            }
        }
        return false;
    }
}