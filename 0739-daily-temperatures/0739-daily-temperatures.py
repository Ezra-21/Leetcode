class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp,stack_index = stack.pop()
                ans[stack_index] = (i-stack_index)

            stack.append([temp,i])


        return ans
