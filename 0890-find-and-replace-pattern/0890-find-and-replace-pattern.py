class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            look_first = {}
            look_second = {}
            flag = True
            for i in range(len(word)):
                if word[i] not in look_first and pattern[i] not in look_second:
                    look_first[word[i]] = pattern[i]
                    look_second[pattern[i]] = word[i]
                    continue

                if word[i] in look_first:
                    if look_first[word[i]] != pattern[i]:
                        flag = False
                        break

                if pattern[i] in look_second:
                    if look_second[pattern[i]] != word[i]:
                        flag = False
                        break

            if flag:
                ans.append(word)

        return ans
                


        