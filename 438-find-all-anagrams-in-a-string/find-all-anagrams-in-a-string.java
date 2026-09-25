class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        HashMap<Character,Integer> mapP = new HashMap<>();
        HashMap<Character,Integer> mapW = new HashMap<>();

        //add p into mapP
        for (int i=0;i<p.length();i++){
            mapP.put(p.charAt(i),mapP.getOrDefault(p.charAt(i),0)+1);
        }
        //declare variables
        int left=0;
        int right=0;
        List<Integer> result = new ArrayList<>(); //syntax doubt

        while(right<s.length()){
            //update window
            mapW.put(s.charAt(right),mapW.getOrDefault(s.charAt(right),0)+1);

            //window length check
            if((right-left+1)>p.length()){
                char ch = s.charAt(left);
                mapW.put(ch,mapW.get(ch)-1);
                if(mapW.get(ch)==0){
                    mapW.remove(ch);
                }
                left++;
            }
            //check frequencies match
            if((right-left+1)==p.length()){
                if (mapP.equals(mapW)){
                    result.add(left);
                }
            }
            right++;
        }
        return result;
    }
}