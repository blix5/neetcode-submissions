import heapq

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        max_heap = []
        while p1 < p2:
            heapq.heappush(max_heap, -min(heights[p1], heights[p2]) * (p2 - p1))
            if heights[p1] < heights[p2]:
                p1 += 1
            elif heights[p2] < heights[p1]:
                p2 -= 1
            else:
                p1 += 1
                p2 -= 1
        return -max_heap[0]

