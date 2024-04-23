class Solution {
    public String intToRoman(int num) {

        // Time Complexity:  O(1)
        // Space Complexity: O(1)

        // Verifies that num is a valid input, if not return nothing
        // Num is supposed to be 1 <= num <= 3999
        if ((num < 1) || (num > 3999)) return "";

        // Each value corresponds to a symbol, simplifies the process of converting num to a roman numeral
        int[] vals = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] syms = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        // StringBuilder object to hold the roman numeral
        StringBuilder roman = new StringBuilder();

        int i = 0;

        // Iterates until num has been fully converted into roman numeral
        while (num > 0) {

            // Checks num to currently looked at val, if larger minuses the value
            // and appends the corresponding symbol
            while (num >= vals[i]) {
                num -= vals[i];
                roman.append(syms[i]);
            }

            i++;
        }

        return roman.toString();
    }
}
