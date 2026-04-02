"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = [intervals[0].end]
        for idx in range(1, len(intervals)):
            i = intervals[idx]
            if i.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)

        return len(heap)
            