# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:33:13 2020

@author: AlvinChen
"""
class Solution1:
    "slow but robust"
    def plusOne(self,A):
        if A:numstr=str(int("".join(list(map(str,A))))+1)
        else:numstr="1"
        numlst=[int(i) for i in numstr]
        return numlst

class Solution:
    "fast but possible overflow"
    def plusOne(self,A):
        A[-1]=A[-1]+1
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
        A= eval(input())
        print(a.plusOne(A))
    except Exception as e:
        print(e)