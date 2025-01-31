class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle = num//3
        summ = 0
        arr = []
        for i in range(middle -1 , middle +2):
            arr.append(i)
            summ+=i
        return arr if summ == num else []
        