// Prints out the ratio for a fraction to the sixth decimal precision
void printRatio(const int &numer, const int &denom) {
    printf("%f\n", (float(numer)/float(denom)));
}

// Finds the amount of elements that are positive, negative, zero and 
// prints the ratio in comparison to total elements
void plusMinus(vector<int> arr) {
    
    // Time Complexity:  O(n)
    // Space Complexity: O(1)
    
    // Variables to hold the amount of positive and negative values
    int pos = 0;
    int neg = 0;
    
    // Variable to hold vector size
    int arrSize = arr.size();
    
    // Loops through every element in vector arr
    for (int el : arr) {
        
        if (el > 0) {
            pos++;
        } else if (el < 0) {
            neg++;
        }
    }
    
    // Prints out the ratio of positive, negative, and zero values
    printRatio(pos, arrSize);
    printRatio(neg, arrSize);
    printRatio((arrSize - neg - pos), arrSize);
}
