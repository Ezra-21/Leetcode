class Solution:
    def countOfSubstrings(self, word: str, kk: int) -> int:
        def solve(k):
            hashh = {'a':0,'e':0,'i':0,'u':0,'o':0}
            check,ans = 0,0
            j = 0
            for i,val in enumerate(word):
                if val in hashh:
                    hashh[val]+=1
                else:
                    check += 1

                while all(val > 0 for val in hashh.values()) and check>=k:
                    ans+=len(word) - i
                    if word[j] in hashh:
                        hashh[word[j]]-=1
                    else:
                        check-=1
                    j+=1

            return ans
 
        return solve(kk) - solve(kk+1)
