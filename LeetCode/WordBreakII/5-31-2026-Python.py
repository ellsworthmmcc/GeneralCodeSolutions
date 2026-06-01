class Solution:
    def _wordRecursive(self, s: str, wordSet: set, memo: dict) -> List[str]:
        if s in memo:
            return memo[s]

        ans = [s] if s in wordSet else []

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in wordSet:
                for result in self._wordRecursive(s[i:], wordSet, memo):
                    ans.append(prefix + " " + result)
        
        memo[s] = ans
        return ans


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Time Complexity: O(n^3)
        # Space Complexity: O(n^2)
        return self._wordRecursive(s=s, wordSet=set(wordDict), memo={})
