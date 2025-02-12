class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left,right = 1 , len(skill)-2
        target = skill[0]+skill[-1]
        ans = skill[0]*skill[-1]
        while left<right:
            if skill[left]+skill[right] == target:
                ans+=(skill[left]*skill[right])
            else:return -1

            left+=1
            right-=1

        return ans 

        