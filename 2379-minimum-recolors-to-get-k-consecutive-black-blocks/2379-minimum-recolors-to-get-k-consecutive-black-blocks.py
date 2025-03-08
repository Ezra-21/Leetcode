class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_white = blocks[:k].count('W')
        op = count_white
        count = count_white
        for i in range(k,len(blocks)):
            if blocks[i] == 'W':
                count+=1
            if blocks[i-k] == 'W':
                count-=1
                
            op = min(op,count)

        return op