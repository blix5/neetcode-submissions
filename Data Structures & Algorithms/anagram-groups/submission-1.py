class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = {}
        for word in strs:
            sort = str(sorted(word))
            if sort in master:
                master[sort].append(word)
            else:
                master[sort] = [word]
        return list(master.values())