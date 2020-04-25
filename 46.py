# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:43:06 2020

@author: AlvinChen
"""
import numpy as np
class Solution:
    def permute(self, nums):
        """
        input type: List[int]
        output type: List[List[int]]
        """
        if not nums: return [[]]
        def getlst(lst):
            rlst=[]
            for i in range(len(lst)):
                olst=getlst(lst[0:i]+lst[i+1:])
                if olst: nlst=[[lst[i]]+j for j in olst]
                else: nlst=[[lst[i]]]
                rlst.extend(nlst)
            return rlst
        return getlst(nums)


if __name__=="__main__":
	s=Solution()
	nums=eval(input())
	print(s.permute(nums))