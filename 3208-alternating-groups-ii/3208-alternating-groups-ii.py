class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        n = len(colors)
        count = 0
        stack = deque()
        for i in range(len(colors)):
            if stack and stack[-1] == colors[i%n]:
                stack.clear()
            stack.append(colors[i%n])
            if len(stack)==k:
                stack.popleft()
                count+=1

        return count