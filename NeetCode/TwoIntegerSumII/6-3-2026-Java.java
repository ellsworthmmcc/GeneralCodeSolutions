class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Two Pointer Solution
        // Time Complexity:  O(n)
        // Space Complexity: O(1)
        
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int res = numbers[left] + numbers[right];
            if (res == target) {
                return new int[]{left + 1, right + 1};
            } else if (res < target) {
                left++;
            } else {
                right--;
            }
        }

        // No valid solution
        return new int[]{-1, -1};
    }
}
