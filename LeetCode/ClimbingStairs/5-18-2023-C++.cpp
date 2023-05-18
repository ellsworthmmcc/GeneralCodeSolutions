class Solution {
public:
    int climbStairs(int n) {

        // Time Complexity:  O(n)
        // Space Complexity: O(1)

        // For cases of 3 or lesser, the amount of distinct ways
        // to climb to the top is the same
        if (n <= 3) {
            return n;
        }

        // Prev to hold the two previous values
        // The amount of distinct ways to climb is equal to the
        // distinct ways to climb n - 1 + n - 2.
        // prev is equal to 3, 2 because starting amount of stairs to climb
        // is 4, holds distinct steps to climb to 3 and 2
        int prev[2] = {3, 2};

        // Variable to hold temporary value in equations
        int temp = 0;

        // Loops until n is reached, finds answer in one iteration
        for (int i = 4; i <= n; i++) {
            temp = prev[0] + prev[1];
            prev[1] = prev[0];
            prev[0] = temp;
        }

        // Returns the amount of distinct ways to climb to the previously
        // amount of steps
        return prev[0];
    }
};
