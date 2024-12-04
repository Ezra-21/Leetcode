class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        ans = 0
        n = len(colors)
        for i in range(n):
            found = True
            for j in range(i,i+2):
                if colors[j%n] == colors[(j+1)%n]:
                    found = False
            if found:
                ans+=1
        return ans

        