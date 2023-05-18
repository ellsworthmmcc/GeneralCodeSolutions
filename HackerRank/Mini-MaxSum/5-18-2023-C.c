// Finds the min and max of the given values in arr
// arr always has atleast 5 integers
void miniMaxSum(int arr_count, int* arr) {
    
    // Time Complexity:  O(n^2)
    // Space Complexity: O(n)
    
    // Variables to hold current max and min
    long long int max = 0;
    long long int min = LLONG_MAX;
    
    // Variable to hold current sum
    long long int currSum = 0;
    
    // Loops through the array twice
    for (int i = 0; i < arr_count; i++) {
        for (int j = 0; j < arr_count; j++) {
            
            // As long as i does not equal j, 
            // add current element to currSum            
            if (i != j) {
                currSum += arr[j];
            }
        }
        
        if (currSum > max) {
            max = currSum;
        } 
        
        if (currSum < min) {
            min = currSum;
        }
        
        currSum = 0;
    }
    
    // Prints out the max and min in long long int format
    printf("%lli %lli \n", min, max);
}
