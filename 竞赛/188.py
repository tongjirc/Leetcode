# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:12:40 2020

@author: AlvinChen
"""

class Solution1:
    def buildArray(self, target, n):
        if not target:return []
        numlst=list(range(1,n+1))
        action=[]
        i=0
        while target[-1]!=numlst[0]:
            if numlst[0]!=target[i]:
                numlst.pop(0)
                action.extend(["Push","Pop"])
            else:
                numlst.pop(0)
                action.extend(["Push"])
                i+=1
        action.extend(["Push"])
        return action

class Solution2:
    def countTriplets(self, lst):
        num=0
        if not lst:return num
        length=len(lst)
        i=0
        while i!=length:
            j=i+1
            a=lst[i]
            while j!=length:
                k=j
                b=lst[j]
                a=a^lst[j]
                while k!=length:
                    b=b^lst[k]
                    if a==b:num+=1
                    k+=1
                j+=1
            i+=1
        return num

import numpy as np
class Solution:
    def minTime(self, n, hasApple):
        if not n:return 0
        hasApple.insert(0,0)
        length=0
        def dfs(root):
            lefthas,righthas=False
            if root*2<=n: lefthas= dfs(root*2)
            if root*2+1<=n: righthas=dfs(root*2+1)
            if lefthas: length+=2
            if righthas: length+=2
            return lefthas or righthas or hasApple[root]=='true'
        return length

if __name__ == "__main__":
    try:
        a = Solution()
        n,lst = eval(input()),input().split(',')
        print(a.minTime(n,lst))
    except Exception as e:
        print(e)
