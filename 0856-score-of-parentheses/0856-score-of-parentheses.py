class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = deque()
        score = 0
        for bracket in s:
            if bracket == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2*score,1)
        
        return score

        
        