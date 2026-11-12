class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for x in nums:
            counts[x] += 1
        sorted_counts = sorted(counts.items(), key=lambda item: item[1])
        return [item[0] for item in sorted_counts[len(sorted_counts)-k:]]
