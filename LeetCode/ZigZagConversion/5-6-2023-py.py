class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        # Base Case
        if numRows == 1:
            return s
        
        # Array of strings equal to number of desired rows
        row_arr = [""] * numRows
        
        # Used to represent current row
        row = 0

        # Value used to increment or decrement row, can be 1 or -1
        val = 1

        # Goes through every value in s and input it into row_arr in a manner
        # that gets the desired ZigZag foramt
        for ch in s:
            row_arr[row] += ch
            
            
            # Reached end of rows, time to decrement
            if row == numRows - 1:
                val = -1
            # Reached beginning of rows, time to increment
            elif row == 0:
                val = 1

            # Changes row num
            row += val
    
        # Returns the joined rows in ZigZag format
        return "".join(row_arr)
