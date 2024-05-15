class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        for i in range(0,m):
            nums.append(nums1[i])
        for i in range(0, n):
            nums.append(nums2[i])
        nums.sort()
        i = 0
        for num in nums:
            nums1[i] = num
            i += 1
        return nums1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj = Solution()
result = obj.merge(nums1, m, nums2, n)
print(result)