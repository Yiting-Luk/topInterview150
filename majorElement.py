class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        uniqNum = []
        count = []
        for num in nums:
            if num not in uniqNum:
                uniqNum.append(num)
                count.append(1)
            else:
                count[-1] += 1
        maxCount = 0
        for i in range(0, len(uniqNum)):
            if count[i] > maxCount:
                majorNum = uniqNum[i]
                maxCount = count[i]
        return majorNum
nums = [3,3,4]
obj = Solution()
result = obj.majorityElement(nums)
print(result)