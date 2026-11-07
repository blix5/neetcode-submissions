class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = {}
        for word in strs:
            if str(sorted(word)) in master:
                master[str(sorted(word))].append(word)
            else:
                master[str(sorted(word))] = [word]
        return list(master.values())