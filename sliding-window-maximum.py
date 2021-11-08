from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        ans = []
        n = len(nums)
        for i in range(n):
            if len(d) == 0:
                d.append(i)
            else:
                while d:
                    if d[0] >= (i - k + 1):
                        break
                    else:
                        d.popleft()
                while d:
                    if nums[d[-1]] < nums[i]:
                        d.pop()
                    else:
                        break
                d.append(i)
            if i >= (k - 1):
                ans.append(nums[d[0]])
        return ans


