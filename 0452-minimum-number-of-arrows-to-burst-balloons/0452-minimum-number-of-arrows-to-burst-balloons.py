class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        s,e = points[0]
        j = 0
        for i in range(len(points)):
            b,t = points[i]
            if b>e:
                j = i
                count+=1
                s,e = points[i]
                continue

            s = max(s,b)
            e = min(e,t)

        return count