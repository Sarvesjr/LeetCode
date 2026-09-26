class Solution {
    public String largestNumber(int[] nums) {
        //convert array to string
        String [] arr = new String[nums.length];
        for(int i=0; i<nums.length; i++){
            arr[i] = String.valueOf(nums[i]);
        }
        //custom sort
        Arrays.sort(arr,(a,b)-> (b+a).compareTo(a+b));

        //base case return 0 if all elements are 0
        if(arr[0].equals("0")){
            return "0";
        }
        
        //build answer - 
        StringBuilder result = new StringBuilder();
        for (String s : arr){
            result.append(s);
        }
        return result.toString();
    }
}