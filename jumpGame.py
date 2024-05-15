class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lenNum = len(nums)
        if lenNum == 1:
            return True
        else:
            ncz = 0
            skip = 0
            for i in range(0, lenNum):
                if nums[i] == 0:
                    ncz += 1
                if nums[i] > 0 and ncz > 0:
                    j = i - ncz - 1
                    minSteps = ncz
                    while j >= 0:
                        if nums[j] > minSteps:
                            skip = 1
                            break
                        minSteps += 1
                        j -= 1
                    if skip == 0:
                        return False
                    else:
                        skip = 0
                elif i == lenNum - 1 and ncz > 0:
                    j = i - ncz
                    minSteps = ncz
                    while j >= 0:
                        if nums[j] >= minSteps:
                            skip = 1
                            break
                        minSteps += 1
                        j -= 1
                    if skip == 0:
                        return False
                    else:
                        skip = 0
            return True

nums = [2,0,1,0,1]
obj = Solution()
result = obj.canJump(nums)
print(result)