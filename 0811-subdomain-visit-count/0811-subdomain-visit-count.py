class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashh = Counter()

        for website in cpdomains:
            
            num,web = website.split(' ')
            arr = web.split('.')
            for i in range(len(arr)):
                hashh['.'.join(arr[i:])] += int(num)

        ans = []
        for val,fre in hashh.items():
            ans.append(str(fre)+' '+val)

        return ans



            
        