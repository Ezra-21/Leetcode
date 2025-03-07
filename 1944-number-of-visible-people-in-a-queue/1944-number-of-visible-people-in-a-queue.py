class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            count = 0
            while stack and stack[-1]<heights[i]:
                stack.pop()
                count+=1
            if stack:
                count+=1
            stack.append(heights[i])
            ans[i] = count

        return ans

            
