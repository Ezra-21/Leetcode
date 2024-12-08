class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split()
        n = len(searchWord)
        index = -1
        for i,word in enumerate(arr):
            if len(word)>=n and word[:n]==searchWord:
                index = i+1
                break
        return index

        