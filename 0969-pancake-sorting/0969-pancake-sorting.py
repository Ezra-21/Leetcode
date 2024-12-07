class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        Max_element = len(arr)
        n = len(arr)
        ans = []

        for i in range(n):
            index = arr.index(Max_element)

            if index == 0:
                arr[:n-i] = arr[:n-i][::-1]
                ans.append(n-i)
            elif 0 < index < n-1:
                arr[:index+1] = arr[:index+1][::-1]
                ans.append(index+1)
                arr[:n-i] = arr[:n-i][::-1]
                ans.append(n-i)
               
            Max_element -= 1

        return ans
               
            


        