class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()


    def _convertChar(self, char: str) -> int:
        # Time Complexity:  O(1)
        # Space Complexity: O(1)
        return ord(char) - ord('a')


    def insert(self, word: str) -> None:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        cur = self.root
        for c in word:
            i = self._convertChar(c)
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True


    def __search(self, prefix) -> TrieNode:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        cur = self.root
        for c in prefix:
            i = self._convertChar(c)
            if cur.children[i] is None:
                return None
            cur = cur.children[i]
        return cur


    def search(self, word: str) -> bool:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        cur = self.__search(word)
        return cur is not None and cur.endOfWord


    def startsWith(self, prefix: str) -> bool:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        cur = self.__search(prefix)
        return cur is not None
