class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = [[height,name] for height,name in zip(heights,names)]
        arr.sort(reverse=True)
        ans = [name for _,name in arr]
        return ans
        
        