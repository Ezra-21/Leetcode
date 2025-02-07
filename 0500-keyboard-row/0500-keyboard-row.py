class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')
        ans = []
        for name in words:
            flag = True
            word = name.lower()
            f,s,t = False,False,False
            if word[0] in first_row:
                f = True
            elif word[0] in second_row:
                s = True
            else:
                t = True
            for char in word:
                if f and char not in first_row:
                    flag = False
                    break
                elif s and char not in second_row:
                    flag = False
                    break
                elif t and char not in third_row:
                    flag = False
                    break
            if flag:
                ans.append(name)
        return ans
                


                


        
        