class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashh = {}
        arr = s.split(' ')
        check = set()

        if len(arr) != len(pattern):
            return False

        for char,word in zip(pattern,arr):
            if word not in hashh and char not in check:
                hashh[word] = char
                check.add(char)
            elif (word not in hashh and char in check) or (word in hashh and char not in check) or (hashh[word] != char):
                return False
        return True

        

