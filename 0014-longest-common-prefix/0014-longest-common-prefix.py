class Solution:
    def longestCommonPrefix(self, name: List[str]) -> str:
        
        res = ""
        i = 0
        while(i<len(name[0])):
            for item in name:
                if i == len(item) or item[i]!=name[0][i]:
                    return res
            res+=name[0][i]
            i+=1
        return res
            
        