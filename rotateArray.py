class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lenNum = len(nums)
        k = k%lenNum      
        copyNum = []
        for num in nums:
            copyNum.append(num)
        left = copyNum[-k:]
        for i in range(0, k):
            copyNum.pop()
        for i in range(0, len(left)):
            nums[i] = left[i]
        for i in range(0, len(copyNum)):
            nums[i+len(left)] = copyNum[i]
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
result = obj.rotate(nums, k)
print(result)