class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedDict = {}
        for i in range(len(position)):
            speedDict[position[i]] = speed[i]
        
        position.sort()

        fleetCnt = 1
        firstP = position.pop()
        prevT = (target - firstP) / speedDict[firstP]
        while position:
            curP = position.pop()
            curExpectT = (target - curP) / speedDict[curP]

            if curExpectT > prevT:
                prevT = curExpectT
                fleetCnt += 1


        return fleetCnt