# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:43:45 2020

@author: AlvinChen

E-mail: nxczx1997@outlook.com

To: GOGOGO
"""

import collections
import time
import copy
import win32com.client as com
import numpy as np
import matplotlib.pyplot as plt
import geojson as geo
from scipy import interpolate

        
def Lst2ListNode(Lst):
    dummy=ListNode(-1,None)
    rcd=dummy
    for i in Lst:
        nd=ListNode(i,None)
        dummy.next=nd
        dummy=dummy.next
    return  rcd.next

def ListNode2Lst(node):
    Lst=[]
    while node:
        Lst.append(node.val)
        node=node.next
    return Lst


class SingleTon(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=object.__new__(cls,*args,**kwargs)
        return cls._instance
    
class ListNode(object):
    _name="ListNode"
    def __init__(self,val=0,next=None,lst=[]):
        if not lst:
            self.val=val
            self.next=next
        else:
            self.val=lst.pop(0)
            if lst:self.next=ListNode(lst=lst)
            else:self.next=None
    def __str__(self):
        return  str(ListNode2Lst(self))
    
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def MergeSort(node):
            if not node or not node.next:return node
            leftNode,rightNode=Split(node)
            left=MergeSort(leftNode)
            right=MergeSort(rightNode)
            return Merge(left,right)

        def Merge(l1,l2):
            if not l1:return l2
            if not l2:return l1
            if l1.val>l2.val:
                l2.next=Merge(l1,l2.next)
                return l2
            else:
                l1.next=Merge(l1.next,l2)
                return l1
        
        def Split(node):
            slow,fast=node,node
            dummy=slow
            while fast and fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            else:
                right=slow.next
                slow.next=None
            return [dummy,right]
            
        return MergeSort(head)

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:return head

        def rotateLst(ihead,now,idepth):
            if not now.next:
                now.next=ihead
                return [idepth,now]
            depth,maybeEnd=rotateLst(ihead,now.next,idepth+1)
            if depth==0:return [depth,maybeEnd]
            elif k%depth==0:return [0,head]
            elif depth-idepth==k%depth:
                newhead=now.next
                now.next=None
                return [0,newhead]
            else:return [depth,maybeEnd]
        
        depth,maybeEnd=rotateLst(head,head,1)
        return maybeEnd
    
    def leastBricks(self, wall):
        if not wall or not wall[0]:return 0
        m=len(wall)
        s=collections.Counter()
        for i in range(m):
            sLine=0
            s[sLine]+=1
            for j in wall[i]:
                sLine+=j
                s[sLine]+=1
        maxs,maxk=0,sum(wall[0])
        for i in s.items():
            if i[0]!=0 and i[0]!=maxk and i[1]>maxs:
                maxs=i[1]
        return m-maxs
        
        
so=Solution()
head=ListNode(lst=[4,2,1,3])
wall=[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
result=so.leastBricks(head,100)
print(result)
