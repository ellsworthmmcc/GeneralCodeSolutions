public class Solution {
    public int RemoveDuplicates(int[] nums) {
        
        // Time Complexity:  O(n)
        // Space Complexity: O(1)

        // Base Case, if only 1 in length, cannot have duplicates
        if (nums.Length == 1) {
            return 1;
        }

        // Count of amount of non-duplicate element
        int count = 0;

        // Loops through all elements in nums
        foreach (int n in nums) {

            // Relies on array being sorted in ascending order
            if (count == 0 || n > nums[count - 1]) {
                nums[count++] = n;
            }
        }

        return count;
    }
}
