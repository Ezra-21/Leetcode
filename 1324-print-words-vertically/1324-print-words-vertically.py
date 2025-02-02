class Solution:
    def printVertically(self, s: str) -> List[str]:
        array = s.split()
        larger_length = 0
        larger_length_index = 0

        for i,word in enumerate(array):
            if len(word)>larger_length:
                larger_length = len(word)
                larger_length_index = i
        
        for i in range(len(array)):
            array[i] = array[i]+' '*(larger_length-len(array[i]))
        
        answer = []

        for i in range(larger_length):
            res = ''
            for j in range(len(array)):
                res+=array[j][i]
            answer.append(res.rstrip())

        return answer

        