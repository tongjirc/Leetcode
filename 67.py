# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:45:36 2020

@author: AlvinChen
"""
class Solution:
    def addBinary(self, a,b):
        c,d=int(a,2),int(b,2)
        str1=""
        e=c+d
        while(e>1):
            str1=str(e%2)+str1
            e=e//2
        if e<2:
            str1=str(e)+str1
        return str1

if __name__=="__main__":
	s=Solution()
	a,b=input(),input()
	print(s.addBinary(a,b))
