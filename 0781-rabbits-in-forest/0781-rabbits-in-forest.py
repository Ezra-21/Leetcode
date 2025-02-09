class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashh = Counter()
        count = 0
        for val in answers:
            if val not in hashh or val == 0:
                hashh[val] = val
                count+=val+1
            else:
                hashh[val] -= 1
                if hashh[val] == 0:
                    del hashh[val] 

        return count