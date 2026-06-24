class Solution:
    def encode(self, strs: List[str]) -> str:
        # Time Complexity:  O(m + n)
        # Space Complexity: O(m + n)
        # m = sum of lengths, n = number of strings

        res = []
        for string in strs:
            res.append(f'{len(string)}#{string}')

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # Time Complexity:  O(m + n)
        # Space Complexity: O(m + n)
        # m = sum of lengths, n = number of strings

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
