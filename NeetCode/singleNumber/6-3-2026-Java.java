class Solution {
    public int singleNumber(int[] nums) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)


        int res = 0;
        for (int num : nums) {
            res ^= num;
        }
        return res;
    }
}
