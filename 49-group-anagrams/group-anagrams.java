class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> group = new HashMap<>();

        for (String word : strs){
            String key = sort(word);
            group.putIfAbsent(key,new ArrayList<>());
            group.get(key).add(word);
        }
        return new ArrayList<>(group.values());
    }
    public String sort(String word){
        char [] arr = word.toCharArray();
        Arrays.sort(arr);
        return new String(arr);
    }
}