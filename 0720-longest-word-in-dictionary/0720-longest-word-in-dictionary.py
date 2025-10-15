class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        sett = set()

        res = ''
        for word in words:
            if word[:-1] in sett:
                if len(res) < len(word):
                    res = word

            sett.add(word)

        return res
