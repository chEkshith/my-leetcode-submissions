class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,r=2,x//2
        while l<=r:
            m=l+(r-l)//2
            sqr=m*m
            if sqr==x:
                return m
            elif sqr<x:
                l=m+1
            else:
                r=m-1
        return r