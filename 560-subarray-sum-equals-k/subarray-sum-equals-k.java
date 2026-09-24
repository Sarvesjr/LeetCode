class Solution {
    public int subarraySum(int[] nums, int k) {
        
        HashMap<Integer, Integer> seen = new HashMap<>();
        seen.put(0,1);
        
        int sum=0;
        int count=0;

        for(int num:nums){
            sum+=num;
            int req=sum-k;

            if(seen.containsKey(req)){
                count+=seen.get(req);
            }
            seen.put(sum,seen.getOrDefault(sum,0)+1);
        }
        return count;
    }
}