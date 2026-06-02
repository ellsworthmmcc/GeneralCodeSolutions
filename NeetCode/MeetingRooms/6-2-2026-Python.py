"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Time Complexity:  O(n log n)
        # Space Complexity: O(n)
        
        # Shallow copy to avoid alterting intervals
        intervalsC = list(intervals)
        intervalsC.sort(key=lambda interval: interval.start)

        for i in range(1, len(intervalsC)):
            if intervalsC[i - 1].end > intervalsC[i].start:
                return False

        return True
