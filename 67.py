# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:45:36 2020

@author: AlvinChen
"""
class Solution1:
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

import collections
class Solution2:
    def addBinary(self, a,b):
        l1,l2=len(a),len(b)
        if l1>l2:b="0"*(l1-l2)+b
        else:a="0"*(l2-l1)+a
        str1,forward="",'0'
        for i in range(max(l1,l2)-1,-1,-1):
            c=collections.Counter([a[i],b[i],forward])
            if c['1']>=2:
                forward='1'
                str1=str(c['1']-2)+str1
            else:
                forward='0'
                str1=str(c['1'])+str1
        else:
            if forward=='1':
                str1='1'+str1
        return str1

import collections
class Solution:
    def addBinary(self, a,b):
        l1,l2=len(a),len(b)
        if l1>l2:b="0"*(l1-l2)+b
        else:a="0"*(l2-l1)+a
        forward='0'
        for i in range(max(l1,l2)-1,-1,-1):
            c=collections.Counter([a[i],b[i],forward])
            if c['1']>=2:
                forward='1'
                a[i]=str(c['1']-2)
            else:
                forward='0'
                a[i]=str(c['1'])+str1
        else:
            if forward=='1':
                a='1'+a
        return a

if __name__=="__main__":
	s=Solution()
	a,b=input(),input()
	print(s.addBinary(a,b))
