class Solution:
    def longestSubarray(self, num: List[int], limit: int) -> int:
        Max_queue = deque()
        Min_queue = deque()
        ans = 0
        j = 0
        for i in range(len(num)):
            while Max_queue and num[Max_queue[-1]]<num[i]:
                Max_queue.pop()
            Max_queue.append(i)

            while Min_queue and num[Min_queue[-1]]>num[i]:
                Min_queue.pop()
            Min_queue.append(i)

            while num[Max_queue[0]] - num[Min_queue[0]]> limit:
                if num[Min_queue[0]] == num[j]:
                    Min_queue.popleft()
                if num[Max_queue[0]] == num[j]:
                    Max_queue.popleft()
                j+=1

            ans = max(ans,i-j+1)

        return ans
        
