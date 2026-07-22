import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap to keep track of the k largest elements
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            # If the heap grows larger than k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # The root of the min-heap is now the kth largest element
        return min_heap[0]
