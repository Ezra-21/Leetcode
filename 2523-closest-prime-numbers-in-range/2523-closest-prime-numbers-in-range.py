class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right<=2:
            return [-1,-1]

        is_prime = [True]*(right+1)
        is_prime[1] = False
        last = int(math.sqrt(right))+1
        for i in range(2,last):
            if is_prime[i]:
                for j in range(i*i,right+1,i):
                    is_prime[j] = False

        prime = [num for num in range(left,right+1) if is_prime[num]]
        if len(prime)<2:
            return [-1,-1]
            
        min_pair = [prime[0],prime[1]]
        min_diff = prime[1] - prime[0]

        for i in range(1,len(prime)-1):
            diff = prime[i+1]-prime[i]
            if min_diff>diff:
                min_pair = [prime[i],prime[i+1]]
                min_diff = diff

        return min_pair

        