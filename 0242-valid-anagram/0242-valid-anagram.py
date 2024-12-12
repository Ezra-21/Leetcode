class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashh1 = Counter(s)
        hashh2 = Counter(t)
        return hashh1==hashh2
        