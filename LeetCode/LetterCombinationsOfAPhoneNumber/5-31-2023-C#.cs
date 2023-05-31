public class Solution {
    public IList<string> LetterCombinations(string digits) {

        // Time Complexity:  O(n^2)
        // Space Complexity: O(n^2)

        // List that holds the possible combinations based on the given digits
        IList<string> possibleCombi = new List<string>();

        // If no digits to check, return empty list
        if (digits.Length == 0) {
            return possibleCombi;
        }

        // Dictionary to hold hold the possible combination based on the digit
        Dictionary<char, string> DigitToCombi = new Dictionary<char, string> {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, 
            {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
        };

        // Integer used to hold the starting count to prevent from going through
        // recently added objects of possibleCombi
        int startingCount = 0;

        // String to hold the possible letter combinations of the examined digit
        string combi;

        // Goes through each digit in digits to find possible combinations
        foreach (char digit in digits) {

            // If possiblecomb is empty, add current possible combinations
            if (possibleCombi.Count() == 0) {
                foreach (char ch in DigitToCombi[digit]) {
                    possibleCombi.Add(ch.ToString());
                }
            // possibleCombi is not empty
            } else {

                // Sets startingCount and combi
                startingCount = possibleCombi.Count();
                combi = DigitToCombi[digit];

                // Goes through every current combination ignoring combinations added later
                for (int i = 0; i < startingCount; i++) {

                    // Goes through every character in combi, adding it to current combinations
                    for (int j = 0; j < combi.Length; j++) {
                        
                        // If last digit of currently added combination, change starting combination
                        if (j == combi.Length - 1) {
                            possibleCombi[i] += combi[j];
                        // Create new combinations based on starting combination and added possible combination
                        } else {
                            possibleCombi.Add(possibleCombi[i] + combi[j]);
                        }
                    }
                }
            }
        }

        return possibleCombi;
    }
}
