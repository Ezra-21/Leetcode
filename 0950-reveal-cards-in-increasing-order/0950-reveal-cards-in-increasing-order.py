class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        ans = [-1]*n
        i,j = 0,0
        flag = True
        while j<n:
            if ans[i%n]==-1:
                if flag:
                    ans[i%n] = deck[j]
                    flag = False
                    j+=1
                else:
                    flag = True
            i+=1

        return ans
