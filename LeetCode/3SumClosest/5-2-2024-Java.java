class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        // Time Complexity:  O(n^2)
        // Space Compliexty: O(1)
        
        // Verifies array is a valid length
        if (nums.length < 3) {
            System.out.println("Invalid Array Length"); 
            return -1;
        }

        // Sorts the array smallest to largest
        Arrays.sort(nums);

        // Gets initial value for closest sum
        int closestSum = nums[0] + nums[1] + nums[2];


        // Loops through entirety of array checking current 
        // element with two elements that follow after it.
        for (int first = 0; first < nums.length - 2; ++first) {
            
            // Skips duplicates, no need to check the same value twice
            if (first > 0 && nums[first] == nums[first - 1]) continue;

            int second = first + 1, third = nums.length - 1;

            // Loops until all values in current window have been checked
            while (second < third) {
                
                int currentSum = nums[first] + nums[second] + nums[third];
                
                if (currentSum == target) return currentSum;

                // Determines if currentSum is closer to target than closestSum.
                if (Math.abs(target - currentSum) < Math.abs(target - closestSum))
                    closestSum = currentSum;

                // If currentSum is greater than target, lowers posssible value of sum
                // Else currentSum is smaller than target, increases possible value of sum
                if (currentSum > target)
                    --third;
                else
                    ++second;
            }
        }

        return closestSum;
    }
}
