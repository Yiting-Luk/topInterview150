import numpy as np
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        lenNum = len(nums)
        numStep = 0
        if lenNum < 2:
            return numStep
        else:
            while i < lenNum - 1:
                maxStep = nums[i]
                if i + maxStep >= lenNum -1:
                    numStep += 1
                    break
                else:
                    allNext = nums[i+1 : i+1+maxStep]
                    j = 0
                    for j in range(0, maxStep):
                        allNext[j] += j
                    j = np.argmax(allNext) + 1
                    i += j
                    numStep += 1
        return numStep


nums = [2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]
obj = Solution()
result = obj.jump(nums)
print(result)
