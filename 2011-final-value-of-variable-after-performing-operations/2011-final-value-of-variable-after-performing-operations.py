class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for char in operations:
            if char[0] == '+' or char[1]=='+':
                ans+=1
            else:
                ans-=1
        return ans
        