class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                stack_index = stack.pop()
                ans[stack_index] = (i-stack_index)

            stack.append(i)


        return ans
