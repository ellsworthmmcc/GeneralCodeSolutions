class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Sliding Window Solution
        // Time Complexity:  O(n)
        // Space Complexity: O(m)
        // n = length of string
        // m = number of unique characters in string

        HashMap<Character, Integer> lastSeen = new HashMap<>();

        int left = 0, longest = 0;

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (lastSeen.containsKey(ch)) {
                left = Math.max(lastSeen.get(ch) + 1, left);
            }

            lastSeen.put(ch, right);
            longest = Math.max(right - left + 1, longest);
        }

        return longest;
    }
}
