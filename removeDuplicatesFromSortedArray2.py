class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length > 2:
            i =2
            while i < length:
                if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                    nums.pop(i)
                    length  = len(nums)
                else:
                    i += 1
            return i
        else: return length
nums = [1,1,1]
obj = Solution()
result = obj.removeDuplicates(nums)
print(result)