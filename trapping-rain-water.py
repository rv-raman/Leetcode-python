class Solution:
    def trap(self, h: List[int]) -> int:
        larr = []
        mx = 0
        n = len(h)
        for i in range(n):
            if mx < h[i]:
                mx = h[i]
            larr.append(mx)

        rarr = [None] * n
        mx = 0
        for i in range(n - 1, -1, -1):
            if mx < h[i]:
                mx = h[i]
            rarr[i] = mx

        ans = 0
        for i in range(n):
            ans += (max(0, min(larr[i], rarr[i]) - h[i]))
        return ans


