class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        sett = set()
        res = ''
        for word in words:
            
            if word[:-1] in sett or len(word)==1:
                sett.add(word)
                if len(res) < len(word):
                    res = word
            
            

        return res
        