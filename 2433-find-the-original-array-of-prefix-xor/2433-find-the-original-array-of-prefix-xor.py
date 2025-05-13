class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        temp = 0
        for num in pref:
            temp1 = temp^num
            ans.append(temp1)
            temp^=temp1
        return ans