class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashh = defaultdict(list)
        for char in strs:
            key = tuple(sorted(char))
            hashh[key].append(char)

        

        return list(hashh.values())

        