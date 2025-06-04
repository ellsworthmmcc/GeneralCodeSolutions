/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    
    // Time Complexity:  O(n)
    // Space Complexity: O(1)

    // Attempts to find the an index where it is not in ascending order
    let i: number = nums.length - 2;
    while ((i >= 0) && (nums[i] >= nums[i + 1])) {
        i--;
    }

    // Reverses if in descending order
    if (i < 0) {
        reverseSubArr(nums, 0, nums.length - 1);
    } else {

        // Attempts to find an index with a larger value
        let j: number = nums.length - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }

        console.log(nums);

        // Swaps i and j
        swapArr(nums, i, j);

        console.log(nums);

        // Reverses the sub-array nums[i + 1]
        reverseSubArr(nums, i + 1, nums.length - 1);
    }
};

// Swaps the values of two indexes of an array
function swapArr(nums: number[], i: number, j:number) {
    [nums[i], nums[j]] = [nums[j], nums[i]];
}

// Reverses the given subarray of an array in-place
function reverseSubArr(nums: number[], start: number, end: number) {
    while (start < end) {
        swapArr(nums, start, end);
        start++;
        end--;
    }
}
