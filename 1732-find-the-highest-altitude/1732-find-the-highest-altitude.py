class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        highest_altitude = 0
        for i in range(len(gain)):
            arr.append(gain[i]+arr[i])
            highest_altitude = max(highest_altitude,arr[-1])

        return highest_altitude

        