
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []  # Stores (value, index) -> Get min value
        max_heap = []  # Stores (-value, index) -> Get max value (since Python has only min-heap)
        j = 0  # Left pointer
        ans = 0
        
        for i in range(len(nums)):
            heappush(min_heap, (nums[i], i))  # Push current value in min-heap
            heappush(max_heap, (-nums[i], i))  # Push negative value in max-heap (for max tracking)

            # Check if the difference between max and min exceeds `limit`
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # Move left pointer to remove invalid elements
                j += 1

                # Remove out-of-window elements
                while min_heap and min_heap[0][1] < j:
                    heappop(min_heap)
                while max_heap and max_heap[0][1] < j:
                    heappop(max_heap)

            # Update the maximum valid window size
            ans = max(ans, i - j + 1)

        return ans
