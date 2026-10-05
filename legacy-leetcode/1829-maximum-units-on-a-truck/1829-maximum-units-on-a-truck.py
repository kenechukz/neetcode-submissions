class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        """
        R:



        return max no. units that can be put in truck (as long as no. boxes < truckSize)

        E:

        if boxTypes.length == 1:

        
        A:

        boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4

        unitsPerBox {0: 3, 1: 2, 2: 1}

        1 * 3 + 2* 2 + 1 * 1 = 8


        """

        boxes = [0] * 1001
        for boxT in boxTypes:
            boxes[boxT[1]] += boxT[0]


        i = 1000
        units = 0
        while truckSize and i > 0:

            if boxes[i] == 0:
                i-=1
                continue
            toLoad = min(truckSize, boxes[i])
            units += toLoad * i
            boxes[i] -= toLoad
            truckSize -= toLoad
            i-=1
            

        return units






        

        

            

            






