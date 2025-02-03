class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashh_s = Counter(s)
        hashh_t = Counter(t)

        return hashh_s == hashh_t

        