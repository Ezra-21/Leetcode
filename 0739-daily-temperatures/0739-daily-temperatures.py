class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n

        for i,temp in enumerate(temperatures):
            if i==0:
                stack.append([temp,i])
                continue
            while stack and stack[-1][0] < temp:
                ans[stack[-1][1]] = i-stack[-1][1]
                stack.pop()

            stack.append([temp,i])


        return ans
