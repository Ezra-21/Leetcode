class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        ans = 0
        n = len(colors)
        for i in range(n):
            if colors[i%n] != colors[(i+1)%n] and colors[(i+1)%n] != colors[(i+2)%n]:
                ans += 1
            
        return ans

        