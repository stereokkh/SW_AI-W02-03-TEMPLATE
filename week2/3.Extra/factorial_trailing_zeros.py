"""
n!에서 맨 뒤 0의 개수
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        k = 1
        cnt = 0
        while n >= self.power(5, k):
            cnt += n//self.power(5,k)
            k+=1            
        return cnt
    def power(self, n, k):
        if k == 0:
            return 1
        return n*self.power(n, k-1)
        