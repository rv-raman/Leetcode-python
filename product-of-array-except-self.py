class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        plist = []
        p=1
        n = len(nums)
        for i in nums:
            p*=i
            plist.append(p)
        p=1
        for i in range(n-1,-1,-1):
            if i==0:
                nums[i]=p
            else:
                x=nums[i]
                nums[i]=plist[i-1]*p
                p*=x
        return nums
