import numpy as np
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        numDays = len(prices)
        if numDays < 2:
            return 0
        maxProfit = float('-Inf')
        for sell in range(1, numDays):
            if prices[sell] > maxProfit:
                diff = prices[sell] - prices[sell-1]
                if diff > 0:
                    currentProfit = prices[sell] - min(prices[0:sell])
                    if currentProfit > maxProfit:
                        maxProfit = currentProfit
        if maxProfit <= 0:
            return 0
        else:
            return maxProfit
                
prices = [1,2]
obj = Solution()
result = obj.maxProfit(prices)
print(result)