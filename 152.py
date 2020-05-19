# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:17:18 2020

@author: AlvinChen
"""

class Solution:
    def maxProduct(self, nums):
        l1=len(nums)
        lst=[]
        lst.append((nums[0],nums[0]))
        for i in range(1,l1):
            plus=max(nums[i],lst[i-1][0]*nums[i],lst[i-1][1]*nums[i])
            minus=min([nums[i],lst[i-1][0]*nums[i],lst[i-1][1]*nums[i]])
            lst.append((plus,minus))
        return max(lst,key=lambda x:x[0])[0]

if __name__=="__main__":
    try:
        a=Solution()
        nums= eval(input())
        print(a.maxProduct(nums))
    except Exception as e:
        print(e)