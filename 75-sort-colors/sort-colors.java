class Solution {
    public void sortColors(int[] nums) {
        int l=0;
        int m=0;
        int h=nums.length-1;

        while (m<=h){
            if(nums[m]==0){
                //put 0 to start
                int temp=nums[l];
                nums[l]=nums[m];
                nums[m]=temp;
                l++;
                m++;
            }
            else if(nums[m]==1){
                //put 1 in middle (already true)
                m++;
            }
            else{
                //put 2 in end
                int temp = nums[m];
                nums[m]=nums[h];
                nums[h]=temp;
                h--;
            }
        }
    }
}