class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1]+=1
                if stack[-1][1] == k:
                    stack.pop()
                continue
            stack.append([char,1])
        
        ans = []
        for val,fre in stack:
            ans.append(val*fre)
        return ''.join(ans)

            
        