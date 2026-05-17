import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        # Time Complexity: O(n log k)
        # Space Complexity: O(n)

        counts = Counter(s)

        if max(counts.values()) > (len(s) + 1) // 2:
            return ""

        # Standard heap is pulling smallest values, we want it pulling largest
        # Make values negative, largest value is now the smallest value
        heap = [(-freq, char) for char, freq in counts.items()]
        heapq.heapify(heap)
        
        result = []
        prev_freq, prev_char = 0, ""

        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char)

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            prev_freq, prev_char = freq + 1, char
        
        return "".join(result)
