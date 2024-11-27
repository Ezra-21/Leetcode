class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        for path in logs:
            if path == '../':
                if stack:
                    stack.pop()
            elif path == './':
                continue
            else:
                stack.append(path)

        return len(stack) 
        