class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashh = Counter(magazine)
        for char in ransomNote:
            if char not in hashh:
                return False
            hashh[char]-=1
            if hashh[char] == 0:
                del hashh[char]

        return True


        