class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            f = 0 - nums[i]
            s = i + 1
            e = n - 1
            sm = 0
            while s < e:
                if s > i + 1 and nums[s] == nums[s - 1]:
                    s += 1
                    continue
                if e < n - 1 and nums[e] == nums[e + 1]:
                    e -= 1
                    continue
                sm = nums[s] + nums[e]
                if sm == f:
                    ans.append([nums[i], nums[s], nums[e]])
                    s += 1
                    e -= 1
                elif sm < f:
                    s += 1
                elif sm > f:
                    e -= 1
        return ans




