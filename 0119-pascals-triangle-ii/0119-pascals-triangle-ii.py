
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = self.getRow(rowIndex - 1)
        curr = [1]
        for i in range(1, len(prev)):
            curr.append(prev[i - 1] + prev[i])
        curr.append(1)
        return curr
