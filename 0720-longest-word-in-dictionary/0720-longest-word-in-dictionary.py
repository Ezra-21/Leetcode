from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  # Sort lexicographically
        sett = set([''])  # Add empty string to handle single-character words
        res = ''
        
        for word in words:
            if word[:-1] in sett:  # Check if the prefix exists
                sett.add(word)
                if len(word) > len(res):
                    res = word
        
        return res
