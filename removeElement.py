class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k
nums = [3,2,2,3]
val = 3
obj = Solution()
result = obj.removeElement(nums, val)
print(result)