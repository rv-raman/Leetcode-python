class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        e = 0
        sm = 0
        n = len(nums)
        ans = 10 ** 5 + 1
        while e < n:
            sm += nums[e]
            while sm >= target:
                ans = min(ans, e - s + 1)
                sm -= nums[s]
                s += 1
            e += 1
        return 0 if ans == 10 ** 5 + 1 else ans
