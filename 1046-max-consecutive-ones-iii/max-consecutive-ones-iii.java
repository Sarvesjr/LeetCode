class Solution {
    public int longestOnes(int[] nums, int k) {
        int i=0;
        int cnt=0;
        int maxi=0;

        for(int j=0;j<nums.length;j++){
            if (nums[j]==0){
                cnt++;
            }
            while(cnt>k){
                if(nums[i]==0){
                    cnt--;
                }
                i++;
            }
            maxi=Math.max(maxi,j-i+1);

        }
        return maxi;
    }
}