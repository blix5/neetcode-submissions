class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        p1 = 0
        p2 = len(height) - 1
        max_height_p1 = height[p1]
        max_height_p2 = height[p2]
        while p1 < p2:
            if max_height_p1 < max_height_p2:
                p1 += 1
                max_height_p1 = max(height[p1], max_height_p1)
                total += max_height_p1 - height[p1]
            elif max_height_p1 > max_height_p2:
                p2 -= 1
                max_height_p2 = max(height[p2], max_height_p2)
                total += max_height_p2 - height[p2]
            else:
                p1 += 1
                p2 -= 1
                max_height_p1 = max(height[p1], max_height_p1)
                max_height_p2 = max(height[p2], max_height_p2)
                if p1 == p2:
                    total += max_height_p1 - height[p1]
                elif p1 < p2:
                    total += max_height_p1 - height[p1]
                    total += max_height_p2 - height[p2]
        return total
        