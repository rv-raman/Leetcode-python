class Solution:
    def recsol(self, n):
        if n <= 2:
            return n
        return self.recsol(n - 1) + self.recsol(n - 2)

    def climbStairs(self, n: int) -> int:
        '''without using any space'''
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c

        '''using arrays O(n) space'''
        # lt = [1,2]
        # for i in range(2,n):
        #     lt.append(lt[i-1]+lt[i-2])
        # return lt[n-1]
        '''recursive'''
        # return self.recsol(n)



