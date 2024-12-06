class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        hashh = {}
        for i in range(len(names)):
            hashh[heights[i]]= names[i]

        heights.sort(reverse=True)

        for i in range(len(names)):
            names[i] = hashh[heights[i]]

        return names