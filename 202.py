# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:08:50 2020

@author: AlvinChen
"""
class Solution1:
    def isHappy(self, n):
        judgelst=set()
        s=n
        while s!=1:
            s,n=0,s
            while n!=0:
                s+=(n%10)**2
                n//=10
            print(s)
            if s in judgelst:return False
            else:judgelst.add(s)
        return True

class Solution:
    """
    fast slow pointer
    """
    def isHappy(self, n):
        def gets(n):
            s=0
            while n!=0:
                s+=(n%10)**2
                n//=10
            return s
        if n==1:return True
        s1=gets(gets(n))
        s2=gets(n)
        if s1==1 or s2==1:return True
        while s1!=s2:
            s1=gets(gets(s1))
            s2=gets(s2)
            if s1==1 or s2==1:return True
        return False

if __name__=="__main__":
    try:
        a=Solution()
        n= eval(input())
        print(a.isHappy(n))
    except Exception as e:
        print(e)