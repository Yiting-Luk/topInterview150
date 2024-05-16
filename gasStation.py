import numpy as np
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        numStation = len(gas)
        offset = np.argmax(gas)
        totalCost = sum(cost)
        totalGas = sum(gas)
        if totalCost > totalGas:
            return -1
        for start0 in range(0, numStation):
            start = start0 + offset
            if start > numStation - 1:
                start = start - numStation
            j = start
            tank = gas[start]
            while j <= start + numStation and tank > 0:
                if j > numStation-1:
                    k = j - numStation
                else:
                    k = j
                tank -= cost[k]
                if tank < 0:
                    break
                else:
                    j += 1
                    if j == start + numStation + 1:
                        return start
                    if j > numStation - 1:
                        k = j - numStation
                    else:
                        k = j    
                    tank += gas[k]
        return -1
gas = [2,0,1,2,3,4,0]
cost = [0,1,0,0,0,0,11]
obj = Solution()
result = obj.canCompleteCircuit(gas, cost)
print(result)
