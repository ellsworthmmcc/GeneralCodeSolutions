class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Time Complexity:  O(log(m x n))
        // Space Complexity: O(1)
        // m is number of rows, n is number of columns
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        final int rows = matrix.length;
        final int cols = matrix[0].length;

        int left = 0;
        int right = rows * cols - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int val = matrix[mid / cols][mid % cols];

            if (target > val) {
                left = mid + 1;
            } else if (target < val) {
                right = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
