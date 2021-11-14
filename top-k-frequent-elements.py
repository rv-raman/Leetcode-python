class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = {}
        for i in nums:
            if i in dt:
                dt[i] += 1
            else:
                dt[i] = 1
        dt = sorted(dt.items(), key=lambda x: x[1], reverse=True)
        return [i for i, j in dt[:k]]

    # return [i for i,j in Counter(nums).most_common(k)]


