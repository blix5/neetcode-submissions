class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = defaultdict(list)
        for word in strs:
            sort = str(sorted(word))
            master[sort].append(word)
        return list(master.values())