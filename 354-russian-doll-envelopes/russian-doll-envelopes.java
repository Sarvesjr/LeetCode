class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        int n = envelopes.length;
        Arrays.sort(envelopes, (a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(b[1], a[1]);
            }
            return Integer.compare(a[0], b[0]);
        });

        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(envelopes[0][1]);

        for (int i = 1; i < n; i++) {
            int height = envelopes[i][1];
            if (height > ans.get(ans.size() - 1)) {
                ans.add(height);
            } else {
                int index = lowerBound(ans, height);
                ans.set(index, height);
            }
        }
        return ans.size();
    }
    private int lowerBound(ArrayList<Integer> ans, int target) {
        int left = 0;
        int right = ans.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (ans.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}