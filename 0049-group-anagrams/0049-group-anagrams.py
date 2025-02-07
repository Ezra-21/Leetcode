class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashh = defaultdict(list)

        for word in strs:
            common = ''.join(sorted(word))
            hashh[common].append(word)
        ans = []
       
        for value in hashh.values():
            ans.append(value)

        return ans
        