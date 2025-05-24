function searchInsert(nums: number[], target: number): number {
    // Time Complexity:  O(log n)
    // Space Complexity: O(1)

    // Assumes given array is sorted in ascending order

    // Variables used for binary search
    let low: number = 0;
    let high: number = nums.length - 1;
    let mid: number;


    while (low <= high) {
        mid = low + Math.floor((high - low) / 2);

        if (nums[mid] === target)
            return mid;
        
        if (nums[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }

    // If target is not found, return the index 
    // it should be inserted into to still be properly sorted
    return low;
};
