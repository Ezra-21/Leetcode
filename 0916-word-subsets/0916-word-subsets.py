class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hashh_word2 = Counter()
        for word in words2:
            fre_word = Counter(word)
            for char in word:
                hashh_word2[char] = max(hashh_word2[char],fre_word[char])

        ans = []

        for word in words1:
            flag = True
            hashh = Counter(word)
            for char,fre in hashh_word2.items():
                if fre>hashh[char]:
                    flag = False
                    break

            if flag:
                ans.append(word)
         
        return ans