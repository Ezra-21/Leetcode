class Solution:
    def frequencySort(self, s: str) -> str:
        hashh = Counter(s)
        hashh_fre = defaultdict(list)
        freq = []
        for val,fre in hashh.items():
            hashh_fre[fre].append(val)
        for fre in hashh_fre:
            freq.append(fre)
        freq.sort(reverse=True)

        ans = []

        for frequency in freq:
            listt = hashh_fre[frequency]
            listt.sort()
            for char in listt:
                ans.extend([char]*frequency)
        return ''.join(ans)


        