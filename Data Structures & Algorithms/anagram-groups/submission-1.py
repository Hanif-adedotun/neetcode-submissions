class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm = {}
        for st in strs:
            key = "".join(sorted(st))
            hashm.setdefault(key, []).append(st)
        
        return list(hashm.values())
        