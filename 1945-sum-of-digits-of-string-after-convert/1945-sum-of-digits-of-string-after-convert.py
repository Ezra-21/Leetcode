class Solution:
    def getLucky(self, s: str, k: int) -> int:
        summ = ''
        for char in s: 
            summ += str(ord(char)-ord('a')+1)

        summ = int(summ)
        
        for _ in range(k):
            
            temp = 0
            while summ:
                temp += summ%10
                summ //= 10
            summ = temp

        return summ

            

