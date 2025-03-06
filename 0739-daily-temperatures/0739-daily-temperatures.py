class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)-1
        stack = []
        ans = [0]*len(temperatures)
        for i,val in enumerate(temperatures[::-1]):
            count = 0
            while stack and temperatures[stack[-1]]<=val:
                count+=ans[stack[-1]]
                stack.pop()

            if stack and temperatures[stack[-1]]>val:
                ans[n-i] = count+1

            stack.append(n-i)

        return ans
