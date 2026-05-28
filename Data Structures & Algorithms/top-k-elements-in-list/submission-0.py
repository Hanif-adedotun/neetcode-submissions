class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        result = []

        c = list(sorted(c.items(), key=lambda x : x[-1], reverse=True))
        
        for i in range(k):
            result.append(c[i][0])
        return result