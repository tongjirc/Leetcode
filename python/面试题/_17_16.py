# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:36:53 2020

@author: AlvinChen
"""
class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)   # 计算 dp[i][0]
            tdp1 = dp0 + nums[i]   # 计算 dp[i][1]
            dp0, dp1 = tdp0, tdp1

        return max(dp0, dp1)

def f(x,i=0):
    if(i==0):
        return((x-4.709)*(x-2.194)*(x-0.097))
    if(i==1):
        return([x/((4.709-2.194)*(4.709-0.097)),x/((2.194-4.709)*(2.194-0.097)),x/((0.097-4.709)*(0.097-2.194))])

if __name__=="__main__":
	s=Solution()
	words=eval(input())
	print(s.massage(words))
