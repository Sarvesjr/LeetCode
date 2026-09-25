class Solution {
    public int search(int[] nums, int target) {
        int n=nums.length;
        int L=0;
        int R=n-1;

        while(L<=R){
            int M=(L+R)/2;

            if(target == nums[M]){
                return M;
            }
            else if(target < nums[M]){
                R=M-1;
            }
            else{
                L=M+1;
            }
        }
        return -1;
    }
}