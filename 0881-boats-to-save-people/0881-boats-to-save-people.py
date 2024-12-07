class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right = 0,len(people)-1
        count = 0
        while left <= right:
            count+=1
            if people[left] + people[right] <=limit:
                left += 1
            right -= 1
        return count


