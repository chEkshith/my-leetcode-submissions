from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # If target is impossible
        if total < abs(target) or (total + target) % 2!= 0:
            return 0

        # This reduces to: count subsets with sum = K
        # where K = (total + target) // 2
        k = (total + target) // 2

        dp = [0] * (k + 1)
        dp[0] = 1 # 1 way to make sum 0

        for num in nums:
            for s in range(k, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[k]