from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        minHeap = [(0, 0)]  # (cost, point_index)
        res = 0
        
        while minHeap:
            cost, i = heapq.heappop(minHeap)
            if visited[i]:
                continue
            visited[i] = True
            res += cost
            
            for j in range(n):
                if not visited[j]:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    heapq.heappush(minHeap, (abs(x1-x2) + abs(y1-y2), j))
        
        return res