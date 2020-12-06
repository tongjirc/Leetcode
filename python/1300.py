# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:51:44 2020

@author: AlvinChen
"""

class Solution:
    def findBestValue(self, arr, target):
        """
        input type:List[int],int
        output type:int
        """
#        arr=copy.copy(nums)
        Length=len(arr)
        arr.sort()
        arr.insert(0,0)
        f=[]
        s=0
        pre=inf
        mindiff,minK=inf,0
        for i in range(0,Length):
            s+=arr[i]
            K1=int((target-s)/(Length-i))
            K2=K1+1
            if abs(target-K1*(Length-i)-s)<=abs(target-K2*(Length-i)-s):
                K=K1
            else:K=K2
            if K>=arr[i+1]:K=arr[i+1]
            elif K<=arr[i]:K=arr[i]
            else:
                pass
            value=K*(Length-i)+s
            diff=abs(target-value)
            if diff>pre:break
            elif diff<mindiff:
                mindiff=diff
                minK=K
            else:pass
            f.append((K,diff))
            pre=diff
        return minK

if __name__=="__main__":
    try:
        a=Solution()
        arr,target= eval(input()),eval(input())
        print(a.findBestValue(arr,target))
    except Exception as e:
        print(e)