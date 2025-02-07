class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hashh = Counter(nums)
        num_pairs,num_leftover = 0,0
        for fre in hashh.values():
            if fre%2==0:
                num_pairs+=fre//2
            else:
                num_pairs+=fre//2
                num_leftover+=1
        return num_pairs,num_leftover





        
        