class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for x in s:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        for y in t:
            if y not in dict:
                return False
            else:
                dict[y] -= 1
                if dict[y] == 0:
                    del dict[y]
        if not dict:
            return True
        return False
            

        
        