class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        d = {}
        for ch in strs :
            s = ''.join(sorted(ch))
            if s in d.keys( ) :
                d[s].append(ch)
            else:
                d[s]=[ch]
        
        for v in d.values():
            out.append(v)

        return out