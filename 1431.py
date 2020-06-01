# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:04:39 2020

@author: AlvinChen
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxnum=max(candies)
        return [i+extraCandies>=maxnum for i in candies]



if __name__=="__main__":
    try:
        a=Solution()
        n= eval(input())
        print(a.generateParenthesis(n))
    except Exception as e:
        print(e)