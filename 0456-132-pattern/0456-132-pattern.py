class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second_min = float('-inf')
        for num in nums[::-1]:
            if num<second_min:
                return True
            while stack and stack[-1]<=num:
                second_min = stack.pop()

            stack.append(num)

        return False

