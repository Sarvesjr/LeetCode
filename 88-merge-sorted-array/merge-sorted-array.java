class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int x= m-1;
        int y= n-1;

        for(int z=m+n-1; z>=0; z--){
            if(x<0){
                nums1[z]=nums2[y]; //copy all y into back
                y--;
            }
            else if(y<0){
                break; //we are done
            }
            else if(nums1[x]>nums2[y]){
                nums1[z]=nums1[x];//put x at back
                x--;
            }
            else{
                nums1[z]=nums2[y];//put y at back
                y--;
            }
        }
    }
}