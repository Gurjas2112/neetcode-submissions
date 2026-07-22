

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

        return max_sum
