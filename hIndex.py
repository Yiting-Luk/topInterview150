from statistics import mean
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sortedCite = sorted(citations, reverse=True)
        numPapers = len(citations)
        left = 0
        right = numPapers-1
        mid = (right+left+1)//2
        if numPapers == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1
        if sum(citations) == 0:
            return 0
        hidx = 1
        while left <= mid and mid <= right and left < right:
            if sortedCite[mid] == (mid + 1):
                hidx = mid + 1
                break
            elif sortedCite[mid] > mid+1:
                hidx = mid + 1
                left = mid
                mid = (right+left+1)//2     
            elif sortedCite[mid] < mid+1:
                right = mid
                mid = (right+left)//2
                if left == mid:
                    break
        return hidx
citations = [11,15]
obj = Solution()
result = obj.hIndex(citations)
print(result)