class Solution {
    private void solve(String digit, StringBuilder output, int i, List<String> ans, String[] mapping) {
        if (i >= digit.length()) {
            ans.add(output.toString());
            return;
        }

        int num = digit.charAt(i) - '0';
        String value = mapping[num];

        for (int j = 0; j < value.length(); j++) {
            output.append(value.charAt(j));
            solve(digit, output, i + 1, ans, mapping);
            output.deleteCharAt(output.length() - 1);
        }
    }

    public List<String> letterCombinations(String digits) {
        List<String> ans = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return ans;
        }
        
        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        solve(digits, new StringBuilder(), 0, ans, mapping);
        return ans;
    }
}