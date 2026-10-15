class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for ch in strs :
            s = ''.join(sorted(ch))
            if s in d.keys( ) :
                d[s].append(ch)
            else:
                d[s]=[ch]
        strs =[]
        for v in d.values():
            strs.append(v)
        return strs