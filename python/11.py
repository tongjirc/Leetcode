# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:19:07 2020

@author: AlvinChen
"""

class Solution1:
    def maxArea(self, height):
        """
        input : List[int]
        output: int
        """
        maxarea=0
        maxhi=0
        N=len(height)
        for i in range(N-1):
            if height[i]<=maxhi:continue
            else: maxhi=height[i]
            maxhj=0
            for j in range(N-1,i,-1):
                if height[j]<=maxhj:continue
                else: maxhj=height[j]
                area=min(height[i],height[j])*(j-i)
                maxarea=max(maxarea,area)
        return maxarea

class Solution:
    def maxArea(self, height):
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

if __name__=="__main__":
    try:
        a=Solution()
        height= eval(input())
        print(a.maxArea(height))
    except Exception as e:
        print(e)