class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = {}
        for i,val in enumerate(s):
            hash[val] = i

        end,i,position = 0,0,0
        ans = []

        while i < len(s):
            position = max(position,hash[s[i]])
            if i == position:
                ans.append(i-end+1)
                end = i+1
            i+=1
            
        return ans