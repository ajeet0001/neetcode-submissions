class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        t = list(t)
        count = Counter(s)
        for c in t:
            count[c] -= 1

        if not any(count.values()):
            return True
        else:
            return False