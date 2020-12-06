# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:51:59 2020

@author: AlvinChen
"""
class Solution:
    def addDigits(self, num: int) -> int:
        while(num>=10):
            newnum=0
            while(num>=10):
                newnum+=num%10
                num=num//10
            newnum+=num
            num=newnum
        return(num)
