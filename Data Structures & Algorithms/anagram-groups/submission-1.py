class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for s in strs:
            
            sorted_s = sorted(s)
            sorted_s = ''.join(sorted_s)
            if sorted_s in d:
                d[sorted_s].append(s)
            else:
                d[sorted_s] = [s]
        for v in d.values():
            ans.append(v)
        return ans