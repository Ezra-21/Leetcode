class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        hashh = {}
        for height,name in zip(heights,names):
            hashh[height] = name

        heights.sort(reverse=True)

        for i,height in enumerate(heights):
            names[i] = hashh[height]
        return names




        