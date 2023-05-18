/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *plusOne(int* digits, int digitsSize, int* returnSize){
    
    // Time Complexity:  O(n)
    // Space Complexity: O(n)

    // Sets the return size to the size of the array
    *returnSize = digitsSize;

    // Allocates the space for the return array
    int *digitsPlus = malloc(*returnSize * sizeof(int));

    // Failure to allocate
    if (digitsPlus == NULL) {
        return NULL;
    }

    // Initializes digitPlus with digits
    memcpy(digitsPlus, digits, *returnSize * sizeof(int));

    // Flag to determine whether loop should continue or not
    bool contFlag = true;

    // Loops until front of digitsPlus is reached or contFlag is false
    for (int i = digitsSize - 1; i >= 0 && contFlag; i--) {
        
        // Adds one to current digit
        digitsPlus[i]++;

        // If digit is 10, set to 0, and add 1 to next digit in next iteration
        if (digitsPlus[i] == 10) {
            digitsPlus[i] = 0;
        // No more addition nessecary
        } else {
            contFlag = false;
        }
    }

    // If digitsPlus[0] is 0, means anothe digit needs to be added to the front
    if (digitsPlus[0] == 0) {

        // Adding new digit place to digitsPlus, return size increases
        (*returnSize)++;

        // Reallocs digitsPlus to make space for extra digit
        digitsPlus = realloc(digitsPlus, *returnSize * sizeof(int));
    
        // Failure to re-allocate
        if (digitsPlus == NULL) {
            return NULL;
        }

        // Shifts digitsPlus over 1 to the right, sets initial int to 1
        memmove(digitsPlus + 1, digitsPlus, digitsSize * sizeof(int));
        digitsPlus[0] = 1;
    }

    return digitsPlus;
}
