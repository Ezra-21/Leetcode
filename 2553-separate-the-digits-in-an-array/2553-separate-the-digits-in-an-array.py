class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            length = math.floor(math.log10(num))+1
            place = 10**(length-1)
            while place:
                first_num = num//place
                ans.append(first_num)
                num%=place
                place//=10
                
        return ans
        