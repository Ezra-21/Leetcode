class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashh = Counter(nums)
        ans = []
        mostFrequent_element = []
        for num,fre in hashh.items():
            mostFrequent_element.append([fre,num])

        mostFrequent_element.sort(reverse=True)
        for i in range(k):
            ans.append(mostFrequent_element[i][1])

        return ans



        
        