import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=sorted(nums1)
        m=sorted(nums2)
        return statistics.median(n+m)
