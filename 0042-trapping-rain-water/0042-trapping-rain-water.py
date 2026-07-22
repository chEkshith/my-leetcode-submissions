class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        k=height.index(max(height))
        l_res=0
        l_max=height[0]
        for i in range(k):
            if height[i]<l_max:
                l_res+=(l_max-height[i])
            else:
                l_max=max(l_max,height[i])
        r_res=0
        r_max=height[-1]
        for i in range(n-1,k,-1):
            if height[i]<r_max:
                r_res+=(r_max-height[i])
            else:
                r_max=max(r_max,height[i]) 
        return l_res+r_res       