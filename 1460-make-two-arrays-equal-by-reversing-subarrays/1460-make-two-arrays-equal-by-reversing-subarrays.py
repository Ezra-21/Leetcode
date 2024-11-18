class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic = Counter(target)
        for val in arr:
            if val not in dic:
                return False

            dic[val] -= 1
            if dic[val] == 0:
                del dic[val]
        
        return True