class Solution {
    fun strStr(haystack: String, needle: String): Int {

        // Time Complexity:  O(n)
        // Space Complexity: O(1)

        // Holds the currently reached element of needle
        var nPos: Int = 0
        // Holds the currently looked at index of haystack
        var idx: Int = 0

        // Goes all the way through haystack
        while (idx < haystack.length) {

            // If current haystack element equal to needle, increment needle position
            if (haystack[idx] == needle[nPos]) {
                nPos++
            // If not equal, slide back and check next character on next iteration
            } else {
                idx -= nPos
                nPos = 0
            }

            // Check if full needle has been found
            if (nPos == needle.length) {

                // Return the starting idx of needle in relation to haystack
                return idx - nPos + 1
            }

            idx++
        }

        // Needle not found
        return -1
    }
}
