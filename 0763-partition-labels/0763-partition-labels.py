class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashh = {}
        for i,val in enumerate(s):
            hashh[val] = i

        ans = []
        end_point = 0
        j = 0
        for i,val in enumerate(s):
            end_point = max(end_point,hashh[val])
            if i == end_point:
                ans.append(i-j+1)
                j = i+1

        return ans


            
        