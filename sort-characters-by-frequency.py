class Solution:
    def frequencySort(self, s: str) -> str:
        # dt={}
        # s = "".join(sorted(s))
        # for i in s:
        #     if i in dt:
        #         dt[i]+=1
        #     else:
        #         dt[i]=1
        # ans="".join(sorted(s,key = lambda x: -dt[x]))
        # return ans
        return "".join([x*y for x,y in Counter(s).most_common()])