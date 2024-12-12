class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashh1 = Counter(s)
        hashh2 = Counter(t)
        return hashh1==hashh2
        