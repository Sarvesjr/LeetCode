class Solution {

    public int[] searchRange(int[] nums, int target) {

        return new int[]{
            findFirst(nums, target),
            findLast(nums, target)
        };
    }

    private int findFirst(int[] nums, int target) {

        int l = 0;
        int r = nums.length - 1;
        int ans = -1;

        while (l <= r) {

            int m = (l + r) / 2;

            if (nums[m] == target) {
                ans = m;
                r = m - 1;       // search left
            }
            else if (nums[m] < target) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }

        return ans;
    }

    private int findLast(int[] nums, int target) {

        int l = 0;
        int r = nums.length - 1;
        int ans = -1;

        while (l <= r) {

            int m = (l + r) / 2;

            if (nums[m] == target) {
                ans = m;
                l = m + 1;       // search right
            }
            else if (nums[m] < target) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }

        return ans;
    }
}