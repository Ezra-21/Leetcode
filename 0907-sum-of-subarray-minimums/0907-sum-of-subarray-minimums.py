class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
    # so find the next and previous smaller number from one point(*number*) then find the distance it have with out including the smaller elements found in the both direction then multiply both distance we get from this we can understand that *number* is minimum for all subarray between that range
        n = len(arr)
        next_smaller = [-1]*n
        prev_smaller = [-1]*n
        stack = []

        for i,num in enumerate(arr):
            while stack and arr[stack[-1]]>num:
                idx = stack.pop()
                next_smaller[idx] = (i-idx)
            if stack:
                idxx = stack[-1]
                prev_smaller[i] = (i-idxx)
            stack.append(i)

        summ = 0
        for i in range(n):
            if next_smaller[i] == -1:
                m1 = (n-i)
            else:
                m1 = next_smaller[i]
            
            if prev_smaller[i] == -1:
                m2 = (i-prev_smaller[i])
            else:
                m2 = prev_smaller[i]
            summ+=(arr[i]*(m1*m2))

        return summ%(10**9 + 7)







            