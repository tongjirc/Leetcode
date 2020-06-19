# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:19:07 2020

@author: AlvinChen
"""

class Solution1:
    def maxScoreSightseeingPair(self, A):
        """
        input : List[int]
        output: int
        """
        maxA=0
        l1=len(A)
        maxbegin,maxend=A[0],A[-1]-l1+1
        begin,end=[],[]
        for i in range(l1-1):
            maxbegin=max(maxbegin,A[i]+i)
            begin.append(maxbegin)
        for i in range(l1-1,-1,-1):
            maxend=max(maxend,A[i]-i)
            end.append(maxend)
        end.reverse()

        for i in range(1,l1-1):
            nowA=begin[i]+end[i]
            if nowA>maxA:maxA=nowA
        return maxA

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        pre_max = A[0] + 0 #初始值
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j) #判断能否刷新res
            pre_max = max(pre_max, A[j] + j) #判断能否刷新pre_max， 得到更大的A[i] + i

        return res

if __name__=="__main__":
    try:
        a=Solution()
        A= eval(input())
        print(a.maxScoreSightseeingPair(A))
    except Exception as e:
        print(e)