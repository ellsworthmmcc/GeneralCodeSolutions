"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Time Complexity:  O(n log n)
        # Space Complexity: O(n)

        time = []

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        startIndex = endIndex = 0

        while startIndex < len(intervals):
            if start[startIndex] < end[endIndex]:
                startIndex += 1
                count += 1
            else:
                endIndex += 1
                count -= 1
            res = max(res, count)

        return res
