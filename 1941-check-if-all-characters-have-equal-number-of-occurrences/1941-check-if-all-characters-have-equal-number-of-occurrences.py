class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashh = Counter(s)
        return all(fre == hashh[s[0]] for fre in hashh.values())
        