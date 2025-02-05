class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hash_chars = Counter(chars)
        hash_check = hash_chars.copy()
        
        ans = 0
        for word in words:
            flag = True
            for char in word:
                if char in hash_check:
                    hash_check[char]-=1
                    if hash_check[char] == 0:
                        del hash_check[char]
                else:

                    flag = False
            if flag:
                
                ans+=len(word)
            hash_check = hash_chars.copy()
            
        return ans
            
        