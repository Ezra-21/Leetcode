class Solution:
    def isValid(self, s: str) -> bool:
        hashh = {')':'(','}':'{',']':'['}
        stack = deque()
        for braket in s:
            if braket not in hashh:
                stack.append(braket)
            else:
                if not stack or stack.pop() != hashh[braket]:
                    return False

        return len(stack) ==0 
        