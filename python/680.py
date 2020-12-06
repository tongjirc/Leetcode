# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:42:55 2020

@author: AlvinChen
"""

class Solution1:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s1,canpop):
            while s1 and s1[0]==s1[-1]:s1=s1[1:-1]
            if not s1:return True
            if canpop:return max(isPalindrome(s1[0:-1],False),isPalindrome(s1[1:],False))
            else:return False
        return isPalindrome(s,True)

class Solution:
    def validPalindrome(self, s1: str) -> bool:
        while s1 and s1[0]==s1[-1]:s1=s1[1:-1]
        if not s1:return True
        else:
            s2,s3=s1[1:],s1[:-1]
            while s2 and s2[0]==s2[-1]:s2=s2[1:-1]
            if not s2:return True
            while s3 and s3[0]==s3[-1]:s3=s3[1:-1]
            if not s3:return True
        return False

if __name__=="__main__":
    try:
        a=Solution()
        n= eval(input())
        print(a.maximalSquare(n))
    except Exception as e:
        print(e)