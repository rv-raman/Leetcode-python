class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # n = len(nums)
        # f=s=0
        # ans=-1
        # for i in range(n):
        #     if nums[i]==0:
        #         f+=1
        #     while f>0 and s<n:
        #         if nums[s]==0:
        #             f-=1
        #         s+=1
        #     ans=max(ans,i-s+1)
        # return ans
        '''linear search approach'''
        c = 0
        ans = 0
        for i in nums:
            if i:
                c += 1
                continue
            ans = max(ans, c)
            c = 0
        ans = max(ans, c)
        return ans

        '''single line solution'''
        # return max(map(len,("".join(map(str,nums))).split('0')))

