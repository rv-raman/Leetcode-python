class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        st = e = 0
        n = len(s)
        dt = {}
        while e < n:
            while st < n and (s[e] in dt) and dt[s[e]] != 0:
                dt[s[st]] = 0
                st += 1
            dt[s[e]] = 1
            ans = max(ans, e - st + 1)
            e += 1
        return ans

