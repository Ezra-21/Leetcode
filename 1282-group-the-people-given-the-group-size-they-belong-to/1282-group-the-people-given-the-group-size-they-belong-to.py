class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashh = defaultdict(list)
        for i,val in enumerate(groupSizes):
            hashh[val].append(i)

        ans = []
        for size,listt in hashh.items():
            i = 0
            while i<len(listt):
                ans.append(listt[i:i+size])
                i+=size

        return ans

        