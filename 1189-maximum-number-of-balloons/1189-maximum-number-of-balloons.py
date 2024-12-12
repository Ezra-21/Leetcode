class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashh = Counter(text)
        return min(hashh.get('b', 0),
                   hashh.get('a', 0),
                   hashh.get('l', 0) // 2,
                   hashh.get('o', 0) // 2,
                   hashh.get('n', 0))
