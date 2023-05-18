class Solution {
    public boolean isMatch(String s, String p) {
        
        // Time Complexity:  O(n^2)
        // Space Complexity: O(n^2)
        
        // If the pattern string is null or empty, return true if 
        // the input string is null or empty, and false otherwise
        if ( p == null || p.isEmpty() ) {
            return (s == null || s.isEmpty());
        }

        // Holds the matrix to help determine if input string does match the pattern
        // All values automatically initialized with false
        boolean state[][] = new boolean[s.length() + 1][p.length() + 1];

        // Setting initial values
        state[0][0] = true;

        // Loops through all of relevant pattern string
        for (int j = 2; j <= p.length(); j++) {
            
            // Sets state to true in cases such as a*b*, where a and b can be nothing
            // and still be true
            state[0][j] = p.charAt(j - 1) == '*' && state[0][j - 2]; 
        }

        // Loops through all of pattern and input string, pattern first
        for (int j = 1; j <= p.length(); j++) {
            for (int i = 1; i <= s.length(); i++) {

                // If input is equal to pattern or input can be anything,
                // set state to true if previous instance of pattern matching was true
                if (p.charAt(j - 1) == s.charAt(i - 1) || p.charAt(j - 1) == '.') {
				    state[i][j] = state[i - 1][j - 1];
                
                // If pattern is zero or more of preceding element, first check whether
                // the preceding element is true and that the previous instance of
                // pattern matching was true
                } else if(p.charAt(j - 1) == '*') {
                    state[i][j] = (state[i][j-2] || 
                        ((s.charAt(i-1) == p.charAt(j-2) || p.charAt(j-2) == '.')) && 
                        state[i-1][j]); 
                }
            }
        }

        // If input string matches the pattern string, should return true, otherwise false
        return state[s.length()][p.length()];
    }
}
