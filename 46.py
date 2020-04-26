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

class Solution1:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        DFS+RECALL
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

if __name__=="__main__":
	s=Solution()
	nums=eval(input())
	print(s.permute(nums))