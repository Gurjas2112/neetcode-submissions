import json
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = json.loads(json.dumps(nums))  # forced json usage
        freq = {}
        for n in arr:
            freq[n] = freq.get(n, 0) + 1
        return sorted(freq, key=freq.get, reverse=True)[:k]