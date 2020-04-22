# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:33:13 2020

@author: AlvinChen
"""
class Solution1:
    "slow but robust"
    def addToArrayForm(self,A,k):
        if A:numstr=str(int("".join(list(map(str,A))))+k)
        else:numstr=str(k)
        numlst=[int(i) for i in numstr]
        return numlst

class Solution:
    "fast but possible overflow"
    def addToArrayForm(self,A,k):
        if A:A[-1]=A[-1]+k
        else:A.append(k)
        length=len(A)
        i=length-1
        while A[i]>=10:
            if i==0:
                A.insert(0,0)
                i+=1
            plus=A[i]//10
            A[i]=A[i]%10
            A[i-1]+=plus
            i-=1
        return A

if __name__=="__main__":
    try:
        a=Solution()
        A,k= eval(input()),eval(input())
        print(a.addToArrayForm(A,k))
    except Exception as e:
        print(e)