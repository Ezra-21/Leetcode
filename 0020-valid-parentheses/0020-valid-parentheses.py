class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        hashh = {')':'(',']':'[','}':'{'}

        for bracket in s:
            if bracket in hashh:
                if not stack or stack.pop()!=hashh[bracket]:
                    return False
            else:
                stack.append(bracket)

        return len(stack) == 0
        