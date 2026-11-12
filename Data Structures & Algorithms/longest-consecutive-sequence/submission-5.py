class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums)
        cons = {}
        for n in set_list:
            if n+1 in cons and n-1 in cons:
                old_cons_neg = cons[n-1]
                old_cons_pos = cons[n+1]
                cons[cons[n+1]] = old_cons_neg
                cons[cons[n-1]] = old_cons_pos
            elif n-1 in cons:
                cons[n] = cons[n-1]
                cons[cons[n-1]] = n
                if cons[n-1] != n:
                    cons.pop(n-1)
            elif n+1 in cons:
                cons[n] = cons[n+1]
                cons[cons[n+1]] = n
                if cons[n+1] != n:
                    cons.pop(n+1)
            else:
                cons[n] = n
        if len(nums) == 0:
            return 0
        return max([v - k + 1 for k, v in cons.items()])