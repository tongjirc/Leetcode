# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:32:09 2020

@author: AlvinChen
"""
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        return x**n

class Solution2:
    def myPow(self, x, n):
        def mult(y,m):
            print(y,m)
            if m==n:return y
            elif n//m>=2:return mult(y*y,m*2)
            else:return mult(y*x,m+1)
        return mult(x,1)

class Solution:
    def myPow(self, x, n):
        binN=bin(abs(n))
        length,i,y,k=len(binN),0,x,1
        while True:
            if binN[length-1-i]=="0":
                pass
            elif binN[length-1-i]=="1":
                k=k*y
            else: break
            i+=1
            y=y*y
        return k if n>=0 else 1/k

if __name__=="__main__":
    try:
        a=Solution()
        x,n= eval(input()),eval(input())
        print(a.myPow(x,n))
    except Exception as e:
        print(e)