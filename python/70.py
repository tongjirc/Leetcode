# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:51:44 2020

@author: AlvinChen
"""
class Solution:
    def climbStairs(self, n):
        """
        input type:int
        output type:int
        """
        if n==0:return 1
        elif n==1:return 1
        elif n==2:return 2
        else:pass
        pre,pree=2,1
        for i in range(2,n):
            now=pre+pree
            pree=pre
            pre=now
        return now


if __name__=="__main__":
    try:
        a=Solution()
        equations= eval(input())
        print(a.climbStairs(equations))
    except Exception as e:
        print(e)