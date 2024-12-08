class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split()
        n = len(searchWord)
        
        for i,word in enumerate(arr):
            if len(word)>=n and word[:n]==searchWord:
                return i+1
        return -1

        