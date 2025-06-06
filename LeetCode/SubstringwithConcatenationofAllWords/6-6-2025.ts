function findSubstring(s: string, words: string[]): number[] {
    
    // Time Complexity: O(n^2)
    // Space Complexity: O(n)

    let wordMap: Map<string, number> = new Map();
    
    let wordLength: number = words[0].length;
    let wordCount: number = words.length;
    let slideWindow: number = wordLength * wordCount;

    // Adds every word to map with count of how many times it appears
    words.forEach(word =>{
        wordMap.has(word) ? wordMap.set(word, wordMap.get(word) + 1) : wordMap.set(word, 1);
    });

    let leftIndex: number = 0;
    let rightIndex: number = slideWindow;
    let result: number[] = [];

    // Checks if a specific subsection contains any order of words
    const helper = (substring) => {
        let visited: Map<string, number> = new Map();
        
        // Adds each substring to visited
        for (let i = 0; i < substring.length; i += wordLength) {
            let word: string = substring.substring(i, i + wordLength);
            
            visited.has(word) ? visited.set(word, visited.get(word) + 1) : visited.set(word, 1);
        }
        
        for (let [key, val] of visited) {
            if (wordMap.get(key) != val) return false;
        }
        
        return true;
    }
    
    // Checks if words can fit in all valid subsections of s
    while (rightIndex <= s.length) {
        if (rightIndex - leftIndex == slideWindow) {
            let substring = s.substring(leftIndex, rightIndex);
            
            if (helper(substring)) result.push(leftIndex);
            
            leftIndex++;
        }
        
        rightIndex++;
    }

    return result;
};
