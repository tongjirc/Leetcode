# -*- coding: utf-8 -*-
"""
Created on Jun  3 17:11:54 2020

@author: AlvinChen
"""

class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second

class Solution:
    def rob(self, nums: List[int]) -> int:
        length=len(nums)
        if length==0:return 0
        dp=[0]*(length+3)
        for i in range(3,length+3):
            dp[i]=nums[i-3]+max(dp[i-2],dp[i-3])
        return max(dp[-1],dp[-2])

if __name__=="__main__":
    try:
        a=Solution()
        b=Solution1()
#        N, K, W= eval(input()),eval(input()),eval(input())
        N, K, W=100,17,1000
        print(a.new21Game(N, K, W))
        print(b.new21Game(N, K, W))
    except Exception as e:
        print(e)