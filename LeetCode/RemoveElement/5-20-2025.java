class Solution {
  public static int removeElement(int[] nums, int val) {

    // Time Complexity:  O(n)
    // Space Complexity: O(1)
    
    // First Pass Solution

    int left = 0;
    int right = nums.length - 1;

    int amountRemoved = 0;

    // Loops through array until every single integer has been
    // looked over once and all invalid values have been moved over
    // to the back of the array
    while (left <= right) {
      if (nums[left] == val) {
        nums[left] = nums[right];
        nums[right] = val;
        right--;
        amountRemoved++;
      } else {
        left++;
      }
    }

    // Returns the amount of valid integers
    return nums.length - amountRemoved;
  }
}
