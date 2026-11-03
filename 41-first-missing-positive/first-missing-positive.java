class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }        
        int i = 1;
        while (numSet.contains(i)) {
            i++;
        }
        return i;
    }
}