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
        else:
            cumProfit = 0
            for sell in range(1, numDays):
                diff = prices[sell] - prices[sell-1]
                if diff > 0:
                    cumProfit += diff
        return cumProfit

prices = [7,1,5,3,6,4]
obj = Solution()
result = obj.maxProfit(prices)
print(result)