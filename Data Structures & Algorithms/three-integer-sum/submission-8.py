class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i-1] == sorted_nums[i]:
                continue
            temp = sorted_nums[i+1:]
            p1 = 0
            p2 = len(temp) - 1
            while p1 < p2:
                if (p1 > 0 and temp[p1] == temp[p1-1]) or temp[p1] + temp[p2] < -sorted_nums[i]:
                    p1 += 1
                    continue
                elif (p2 < len(temp)-1 and temp[p2] == temp[p2+1]) or temp[p1] + temp[p2] > -sorted_nums[i]:
                    p2 -= 1
                    continue
                else:
                    item = [sorted_nums[i], sorted_nums[p1+i+1], sorted_nums[p2+i+1]]
                    output.append(item)
                    p1 += 1
                    p2 -= 1
            
        return output