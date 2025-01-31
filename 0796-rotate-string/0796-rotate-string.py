class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal)!=len(s):
            return False

        check = s*2
        return True if goal in check else False