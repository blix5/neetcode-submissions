class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod1 = 1
        prod2 = 1
        prod2hist = [1]
        for i in range(len(nums)-1):
            prod2 *= nums[len(nums)-1-i]
            prod2hist.append(prod2)
        output = [prod2hist[len(prod2hist)-1]]
        for i in range(len(nums)-1):
            prod1 *= nums[i]
            output.append(prod1 * prod2hist[len(prod2hist)-2-i])
        return output
