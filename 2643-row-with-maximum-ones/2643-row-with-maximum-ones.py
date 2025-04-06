class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        hashh = defaultdict(list)
        arr = []
        for i,row in enumerate(mat):
            count = row.count(1)
            arr.append(count)
            hashh[count].append(i)
        arr.sort()
        return hashh[arr[-1]][0],arr[-1]
