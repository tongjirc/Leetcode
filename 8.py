# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:12:40 2020

@author: AlvinChen
"""
class Solution:
    def myAtoi(self, str1):
        str1=str1.strip(' ')
        N=len(str1)
        suffNum=0 #suffNumber=suffNum+1
        sign=""
        if N>0 and str1[0] in "+-":
            sign=str1[0]
            str1=str1[1:]
            N-=1
        while(0<=suffNum<N and str1[suffNum] in "1234567890"):
            suffNum+=1
        if suffNum==0:
            return 0
        else:
            num=int(sign+str1[:suffNum])
            if num>2**31-1:
                num=2**31-1
            if num<-2**31:
                num=-2**31
            return num



if __name__=="__main__":
    try:
        a=Solution()
        str1= input()
        print(a.myAtoi(str1))
    except Exception as e:
        print(e)