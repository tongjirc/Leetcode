# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:08:43 2020

@author: AlvinChen
"""
import collections
class Solution1:
    def singleNumbers(self, nums):
        c=collections.Counter(nums)
        lst=sorted(c.items(),key=lambda x:x[1])
        return [lst[0][0],lst[1][0]]

class Solution2:
    def singleNumbers(self, nums):
        nums.sort()
        rlst=[nums[0]]
        for i in nums[1:]:
            print(i,rlst)
            if rlst and i==rlst[-1]:rlst.pop()
            else:rlst.append(i)
        return rlst

class Solution:
    def singleNumbers(self, nums):
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


if __name__=="__main__":
	s=Solution()
	nums=eval(input())
	print(s.singleNumbers(nums))

