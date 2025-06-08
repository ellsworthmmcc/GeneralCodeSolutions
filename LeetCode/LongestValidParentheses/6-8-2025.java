class Solution {
    public int longestValidParentheses(String s) {
        
        // Time Complexity:  O(n)
        // Space Complexity: O(n)

        // If  no valid parenthese are possible, return 0
        if (s.length()  <= 1) return 0;

        int[] dp = new int[s.length()];
        int longest = 0, leftParentheses = 0;

        // Loops through every character in s once
        for (int i = 0; i < s.length(); i++) {

            if (s.charAt(i) == '(') {
                leftParentheses++;
            } else if (leftParentheses > 0){
                
                // If previous index of dp is not 0, means consecutive left and then right parentheses
                dp[i] = dp[i - 1] + 2;

                // If there is an amount of previous valid parentheses, add it to current
                // if not, add 0
                dp[i] += (i - dp[i]) >= 0 ? dp[i - dp[i]] : 0;
                longest = Math.max(longest, dp[i]);
                leftParentheses--;
            }
        }

        return longest;
    }
}
