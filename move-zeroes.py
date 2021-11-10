# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         j = 0
#         n = len(nums)
#         for i in range(n):
#             if nums[i] != 0:
#                 nums[j] = nums[i]
#                 j += 1
#         for i in range(j, n):
#             nums[i] = 0
#         return nums
'''two pointer approach'''


class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        j = 0
        for i in range(n):
            if arr[i] != 0 and arr[j] == 0:
                arr[i], arr[j] = arr[j], arr[i]
            if arr[j] != 0:
                j += 1
        return arr






