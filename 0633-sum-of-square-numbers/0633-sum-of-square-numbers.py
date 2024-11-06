class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        total = 0
        collection = []
        for i in range(int(math.sqrt(c))+1):
            collection.append(i)

        right,left = len(collection)-1,0

        while left<=right:
            target = collection[left]**2 + collection[right]**2
            if target == c:
                return True
            elif target > c:
                right -= 1
            else:
                left += 1
        return False
