# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:32:09 2020

@author: AlvinChen
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n



if __name__=="__main__":
    try:
        a=Solution()
        str1= input()
        print(a.myAtoi(str1))
    except Exception as e:
        print(e)