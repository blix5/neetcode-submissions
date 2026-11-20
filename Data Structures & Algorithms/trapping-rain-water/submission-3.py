class Solution:
    def trap(self, height: List[int]) -> int:
        suffix_max = [0] * len(height)
        max_height = 0
        for i in range(len(height)):
            max_height = max(max_height, height[len(height)-1-i])
            suffix_max[len(height)-1-i] = max_height

        prefix_max = [0] * len(height)
        max_height = 0
        sum = 0
        for i in range(len(height)):
            max_height = max(max_height, height[i])
            prefix_max[i] = max_height
            sum += min(prefix_max[i], suffix_max[i]) - height[i]
            
        return sum