class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        bit_count = [0] * (501)  

        for num in nums:
            bit_count[num] ^= 1  
        return sum(bit_count) == 0  