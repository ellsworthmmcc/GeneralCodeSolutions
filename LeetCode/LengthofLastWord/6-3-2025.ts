function lengthOfLastWord(s: string): number {
    
    // Time Complexity:  O(n)
    // Space Complexity: O(1)

    let length:number = 0;
    let index:number = s.length - 1;

    // Finds end of last word
    while (!isLetter(s.charAt(index)) && index >= 0) {
        index--;        
    }

    // Counts the letters of the last word
    for (index; index >= 0 && isLetter(s.charAt(index)); index--) {
        length++;
    }

    return length;
};

// Checks if a given character is a letter
function isLetter(ch: string): boolean {
    if (ch.length === 1) {
        return ch.toLowerCase() !== ch.toUpperCase();
    }

    return false;
}
