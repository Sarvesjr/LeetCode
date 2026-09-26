class Solution {
    public int[][] merge(int[][] intervals) {
        // Sort by starting value
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> output = new ArrayList<>();
        output.add(intervals[0]);

        // Check remaining intervals
        for (int i = 1; i < intervals.length; i++) {

            int start = intervals[i][0];
            int end = intervals[i][1];

            // Last interval in output
            int[] last = output.get(output.size() - 1);

            // Overlap
            if (start <= last[1]) {

                // Extend the end
                last[1] = Math.max(last[1], end);

            }
            else {

                // No overlap
                output.add(new int[]{start, end});
            }
        }

        return output.toArray(new int[output.size()][]);
    }
}