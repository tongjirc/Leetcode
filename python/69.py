# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:13:40 2020

@author: AlvinChen
"""
class Solution:
    def mySqrt(self, x):
        """
        input type: int
        output type: int
        Newton Method
        """
        x0,eps=1,1e-4
        x1=2
        while abs(x1-x0)>eps:
            x0=x1
            x1=(x0+x/x0)/2
        return int(x1)



if __name__=="__main__":
    try:
        a=Solution()
        n= eval(input())
        print(a.mySqrt(n))
    except Exception as e:
        print(e)