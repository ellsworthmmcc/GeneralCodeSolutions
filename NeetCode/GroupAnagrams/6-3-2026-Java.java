class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Time Complexity:  O(n * k)
        // Space Complexity: O(n * k)
        
        Map<String, List<String>> anagramMap = new HashMap<>();
        
        for (String str : strs) {
            int[] count = new int [26];
            for (char c : str.toCharArray()) {
                count[c - 'a']++;
            }
            String strKey = Arrays.toString(count);

            anagramMap.computeIfAbsent(strKey, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(anagramMap.values());
    }
}
