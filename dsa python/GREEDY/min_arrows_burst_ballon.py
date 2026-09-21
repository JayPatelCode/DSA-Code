points = [[10,16],[2,8],[1,6],[7,12]]
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        x=points[0]
        last_arrow=points[0][1]
        count=1
        for i in range(1,len(points)):
            if last_arrow<points[i][0]:
                count+=1
                last_arrow=points[i][1]
        return count

s=Solution()

print(s.findMinArrowShots(points=points))