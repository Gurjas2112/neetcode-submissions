class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency manually using a dictionary
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Step 2: Create buckets where index = frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in freq_map:
            freq = freq_map[num]
            bucket[freq].append(num)

        # Step 3: Gather top k frequent elements from the buckets
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
