# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:51:44 2020

@author: AlvinChen
"""

class Solution1:
    def search(self, nums, target):
        return nums.index(target) if nums.count(target)>0 else -1

class Solution:
    def search(self, nums, target: int):
        length=len(nums)

        def findkey(lw,hi):
            if nums[hi]>=nums[lw]:return hi
            while nums[hi]<nums[lw]:
                mid=(lw+hi)//2
                if mid==lw:return lw
                if nums[lw]<nums[mid]:lw=mid
                else:hi=mid-1
            return hi

        def findtarget(lst,t,plus):
            lw,hi=0,len(lst)-1
            if not lst:return -1
            while hi>=lw:
                mid=(hi+lw)//2
                if lst[mid]>t:hi=mid-1
                elif lst[mid]<t:lw=mid+1
                else:return mid+plus
            else:return -1

        if not nums:return -1
        else:key=findkey(0,length-1)
        if nums[0]<=target<=nums[key]:
            flst,plus=nums[0:key+1],0
        elif key+1<=length-1 and nums[key+1]<=target<=nums[length-1]:
            flst,plus=nums[key+1::],key+1
        else:return -1
        return findtarget(flst,target,plus)


if __name__=="__main__":
    try:
        a=Solution()
        nums,target= eval(input()),eval(input())
        print(a.search(nums,target))
    except Exception as e:
        print(e)