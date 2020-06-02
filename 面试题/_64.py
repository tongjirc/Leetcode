# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:12:40 2020

@author: AlvinChen
"""
class Solution:
    def sumNums(self, n: int) -> int:
        n & n+=sumNums(n-1)
        return n



if __name__=="__main__":
    try:
        a=Solution()
        n= eval(input())
        print(a.generateParenthesis(n))
    except Exception as e:
        print(e)