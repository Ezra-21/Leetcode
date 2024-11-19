class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)
        k = k % total
        i = 0
        while(True):
            if chalk[i%n] > k:
                return i%n
            k -= chalk[i%n]
            i+=1

        