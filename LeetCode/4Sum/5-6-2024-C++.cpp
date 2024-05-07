class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        // Time Complexity:  O(n^3)
        // Space Complexity: O(1)

        // Variable representing the size of nums
        int n = nums.size();

        vector<vector<int>> uniqueQuadruplets;

        // Impossible to have a unique quadruplet equaling target
        // if there are not atleast 4 elements
        if (n < 4) {
            return uniqueQuadruplets;
        }

        // Sorts the vector to allow more optimized finding of the four sums
        sort(nums.begin(), nums.end());


        // Loops through the vector checking every possible unique combination of four numbers
        for (int i = 0; i < n - 3; ++i) {

            // Loops following after i to avoid checking things already checked
            for (int j = i + 1; j < n - 2; ++j) {

                // Long long is used because every num has the possibility of being a maximum or minimum int
                long long newTarget = (long long)target - (long long)nums[i] - (long long)nums[j];
                
                int low = j + 1, high = n- 1;

                // Loops until low is higher than high, meaning this section of the vector has been checked
                while(low < high) {

                    // If lesser than newTarget, need to increase value so increment low to a greater number
                    if (nums[low] + nums[high] < newTarget) ++low;
                    // If higher than newTarget, need to decrease value so decrement high to a lesser number
                    else if (nums[low] + nums[high] > newTarget) --high;
                    // newTarget has been found
                    else {
                        uniqueQuadruplets.push_back({nums[i], nums[j], nums[low], nums[high]});

                        // Variables used to keep track of low and high to avoid duplicates
                        int tempLow = low, tempHigh = high;

                        // Increments low and high until duplicates have been passed
                        while(low < high && nums[low] == nums[tempLow]) ++low;
                        while(low < high && nums[high] == nums[tempHigh]) --high;
                    }
                }

                // Increments j until duplicates have been passed
                while((j + 1 < n) && (nums[j] == nums[j + 1])) ++j;
            }

            // Increments i until duplicates have been passed
            while((i + 1 < n) && (nums[i] == nums[i + 1])) ++i;
        }

        return uniqueQuadruplets;
    }
};
