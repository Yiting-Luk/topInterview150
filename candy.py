import numpy as np
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        numChild = len(ratings)
        if numChild == 1:
            return 1
        
        diffs = np.diff(ratings)
        candy = []
        i = 0
        while i < numChild:
            currentCandy = 1 
            # left prominent
            if i > 0:
                if diffs[i-1] > 0:
                    currentCandy = candy[-1]+1
            cnt = 0
            if i < numChild - 1:
                if diffs[i] < 0:                   
                    for j in range(i, numChild-1):
                        if diffs[j] < 0:
                            cnt += 1
                        if diffs[j] >= 0:
                            break
                    if cnt+1 > currentCandy:
                        currentCandy = cnt+1
            candy.append(currentCandy)
            i += 1
            if cnt > 0:
                while cnt > 0:
                    candy.append(cnt)
                    cnt -= 1
                    i += 1
        # return sum(candy)
        return candy
ratings = [1,3,4,5,2]
obj = Solution()
result = obj.candy(ratings)
print(result)