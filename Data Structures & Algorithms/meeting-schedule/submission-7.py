"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Node:
    def __init__(self, i, l, r):
        self.i = i
        self.l = l
        self.r = r

class Tree:
    def __init__(self, root):
        self.root = root

    def add(self, i):
        curr = self.root
        while True:
            if i.end > curr.i.start and i.start < curr.i.end:
                return False
            
            if i.end < curr.i.start: 
                if curr.l is None:
                    curr.l = Node(i, None, None)
                    return True
                else:
                    curr = curr.l
            else: 
                if curr.r is None:
                    curr.r = Node(i, None, None)
                    return True
                else:
                    curr = curr.r


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        
        root = Tree(Node(intervals[0], None, None))
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if root.add(interval) == False:
                return False

        return True



