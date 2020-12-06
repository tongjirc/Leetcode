# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:43:48 2020

@author: AlvinChen
"""
class MountainArray:
    def __init__(self,lst):
        self.lst=lst
    def get(self, index: int) -> int:
        return self.lst[index]
    def length(self) -> int:
        return len(self.lst)

import numpy as np
class Solution:
    def findInMountainArray(self, target, moutainlst):
        """
        input type:
            int
            MountainArray
        output type:
            int
        """
        moutain=MountainArray(moutainlst)
        length=moutain.length()
        LEFT,RIGHT=0.3819660112501051,0.6180339887498949
        if length==0:return -1

        def gettop(moutain,lw,hi):
            """
            get top index within lw,hi index
            """
            left,right=int((hi-lw)*LEFT+lw),int(np.ceil((hi-lw)*RIGHT+lw))
            leftValue,rightValue=moutain.get(left),moutain.get(right)
            while lw!=left and hi!=right:
                sign2=np.sign(rightValue-leftValue)
                if sign2==1 :
                    lw=left
                    left,leftValue=right,rightValue
                    right=int(np.ceil((hi-lw)*RIGHT+lw))
                    rightValue=moutain.get(right)
                elif sign2==-1:
                    hi=right
                    right,rightValue=left,leftValue
                    left=int((hi-lw)*LEFT+lw)
                    leftValue=moutain.get(left)
                elif left!=right and sign2==0:
                    lw,hi=left,right
                    left,right=int((hi-lw)*LEFT+lw),int(np.ceil((hi-lw)*RIGHT+lw))
                    leftValue,rightValue=moutain.get(left),moutain.get(right)
                else:break
            return max(range(lw,hi+1),key=lambda x:moutain.get(x))

        def getindex(moutain,tvalue,lw,hi,reverse=False):
            """
            get the target index within lw,hi index
            """
            while hi>=lw:
                mid=(lw+hi)//2
                midvalue=moutain.get(mid)
                if (tvalue>midvalue and not reverse) or (tvalue<midvalue and reverse):lw=mid+1
                elif (tvalue<midvalue and not reverse) or (tvalue>midvalue and reverse):hi=mid-1
                else:return mid
            else:return -1
        topind=gettop(moutain,0,length-1)
        left=getindex(moutain,target,0,topind,reverse=False)
        if left!=-1: return left
        if topind<length-1:right=getindex(moutain,target,topind+1,length-1,reverse=True)
        else:return -1
        return right


if __name__=="__main__":
    try:
        a=Solution()
        moutainlst, target= eval(input()),eval(input())
        print(a.findInMountainArray(target, moutainlst))
    except Exception as e:
        print(e)