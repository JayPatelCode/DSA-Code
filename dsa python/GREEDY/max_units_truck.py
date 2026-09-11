from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total = 0

        for boxes, units in boxTypes:
            take = min(boxes, truckSize)

            total += take * units
            truckSize -= take

            if truckSize == 0:
                break

        return total
    
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
s=Solution()

print(s.maximumUnits(boxTypes=boxTypes,truckSize=truckSize))