class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashh = defaultdict(list)
        for dirr in paths:
            filee = dirr.split()
            for i in range(1,len(filee)):
                dirr1,content = filee[i].split('(')
                hashh[content[:-1]].append(filee[0]+'/'+dirr1)

        ans = []
        for value in hashh.values():
            if len(value)>1:
                ans.append(value)

        return ans

