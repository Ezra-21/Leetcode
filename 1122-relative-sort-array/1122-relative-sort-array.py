class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for val in arr2:
            for num in arr1:
                if val == num:
                    ans.append(num)
        arr1.sort()
        for val in arr1:
            if val not in arr2:
                ans.append(val)

        return ans
        