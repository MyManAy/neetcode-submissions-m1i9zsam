class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = [(p[0]**2 + p[1]**2, p) for p in points]

        heapq.heapify(heap)

        final = []
        for i in range(k):
            final.append((heapq.heappop(heap))[1])

        return final
        
        
        