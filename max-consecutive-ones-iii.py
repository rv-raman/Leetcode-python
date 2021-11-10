class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = 0
        s = 0
        ans = -1
        for i in range(n):
            if nums[i] == 0:
                f += 1
            while f > k and s < n:
                if nums[s] == 0:
                    f -= 1
                s += 1
            ans = max(ans, i - s + 1)
        return ans

