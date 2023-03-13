import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = [-s for s in stones]  # negative values so equivalent to min heap
        heapq.heapify(heap)

        while len(heap) > 1:
            y = abs(heapq.heappop(heap))
            x = abs(heapq.heappop(heap))
            if x != y:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if len(heap) > 0 else 0