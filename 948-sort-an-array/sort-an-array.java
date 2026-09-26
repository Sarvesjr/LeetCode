class Solution {
    public int[] sortArray(int[] nums) {
        if(nums.length > 1){
            int mid=(nums.length)/2;

            int [] L = new int[mid];
            int [] R = new int[nums.length - mid];

            for(int i=0;i<mid;i++){
                L[i]=nums[i];
            }
            for(int i=mid;i<nums.length;i++){
                R[i-mid]=nums[i];
            }
            sortArray(L);
            sortArray(R);
            
            int i=0;
            int j=0;
            int k=0;

            while(i<L.length && j<R.length){
                if(L[i]<R[j]){
                    nums[k] = L[i];
                    i++;
                }
                else{
                    nums[k] = R[j];
                    j++;
                }
                k++;
            }
            while(i<L.length){
                nums[k] = L[i];
                i++;
                k++;
            }
            while(j<R.length){
                nums[k] = R[j];
                j++;
                k++;
            }
        }
        return nums;
    }
}