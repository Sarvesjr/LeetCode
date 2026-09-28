class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> map = new HashMap<>();
        Stack <Integer> stack = new Stack<>(); //store num:next greater num
        
        for(int x : nums2){
            while(!stack.isEmpty() && stack.peek() < x ){
                map.put(stack.pop(),x); //if x is less than top then pop the top, add x as next greater value of top to the map
            }
            stack.push(x); //push value to stack if empty
        }
        
        for(int i = 0; i<nums1.length; i++){
            nums1[i] = map.getOrDefault(nums1[i],-1); //for each value, return its next greater element from map or -1 is none
        }
        return nums1;
    }
}