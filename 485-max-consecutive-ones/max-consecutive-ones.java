class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int l = 0, result = 0;
        for (int r=0;r<nums.length;r++){
            if(nums[r]==0){
                l=r+1;
            }
            else{
                result = Math.max(result, r-l+1);
            }
        }
        return result;
    }
}