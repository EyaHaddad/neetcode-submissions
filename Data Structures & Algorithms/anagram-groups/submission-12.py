class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for ch in strs :
            s = ''.join(sorted(ch))
            d[s] = [ch] if s not in d else d[s] + [ch]
        return list(d.values())