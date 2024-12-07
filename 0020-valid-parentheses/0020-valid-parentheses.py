class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = { '}':'{',']':'[',')':'(' }
        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            else:
                if not stack or stack.pop() != bracket_map[bracket]:
                    return False
        return not stack

            
        