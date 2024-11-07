class Solution:
    def dividePlayers(self, skill: List[int]) -> int: 
        skill.sort()
        left,right = 0,len(skill)-1
        target = skill[0] + skill[-1]
        ans = 0
        while left < right:
            if skill[left] + skill[right] == target:
                ans += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
        return ans

        