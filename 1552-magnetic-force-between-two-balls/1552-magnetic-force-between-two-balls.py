class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            count = 1
            last_pos = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_pos >= mid:
                    count += 1
                    last_pos = position[i]
                    
            if count>=m:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        
        return ans
