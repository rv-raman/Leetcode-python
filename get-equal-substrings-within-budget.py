class Solution:
    def equalSubstring(self, s: str, t: str, m: int) -> int:
        # n = len(s)
        # ans=0
        # for i in range(n):
        #     c=0
        #     for j in range(i,n):
        #         c+=(abs(ord(t[j])-ord(s[j])))
        #         if c<=m:
        #             ans = max(ans,j-i+1)
        #         else:
        #             break
        # return ans
        start = end = 0
        n = len(s)
        c = 0
        ans = 0
        while end < n:
            c += (abs(ord(t[end]) - ord(s[end])))
            while c > m:
                c -= (abs(ord(t[start]) - ord(s[start])))
                start += 1
            ans = max(ans, end - start + 1)
            end += 1
        return ans



