class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        presum = []
        dt = {}
        n = len(nums)
        for i in range(n):
            if i == 0:
                presum.append(nums[i])
            else:
                presum.append(nums[i] + presum[i - 1])
            if presum[i] == k:
                ans += 1
            if presum[i] - k in dt:
                ans += (dt[presum[i] - k])
            if presum[i] in dt:
                dt[presum[i]] += 1
            else:
                dt[presum[i]] = 1
        return ans
