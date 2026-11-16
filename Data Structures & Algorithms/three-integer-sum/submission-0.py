class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            temp = sorted_nums[i+1:]
            p1 = 0
            p2 = len(temp) - 1
            for j in range(len(temp)):
                if p1 >= p2:
                    break
                elif temp[p1] + temp[p2] == -sorted_nums[i]:
                    item = [sorted_nums[i], sorted_nums[p1+i+1], sorted_nums[p2+i+1]]
                    if item not in output:
                        output.append(item)
                    p1 += 1
                    p2 -= 1
                elif temp[p1] + temp[p2] > -sorted_nums[i]:
                    p2 -= 1
                else:
                    p1 += 1
            
        return output