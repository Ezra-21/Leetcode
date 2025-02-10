class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        hashh = {}
        for height,name in zip(heights,names):
            hashh[height] = name

        for i in range(len(heights)):
            for j in range(len(heights)-1):
                if heights[j]<heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
                    
        for i,height in enumerate(heights):
            names[i] = hashh[height]
        return names




        