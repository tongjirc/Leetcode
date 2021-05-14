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
    
    def cuttingRope(self, n):
        if n>3:
            if n%3==0:return 3**(n//3)
            elif n%3==1:return 3**(n//3-1)*4
            else: return 3**(n//3)*2
        else:
            return 1*(n-1)
        
    def leafSimilar(self, root1, root2):
        
        def dfsLst(root):
            dfsLst1,lst1=[root],[]
            while dfsLst1:
                node=dfsLst1.pop()
                if node.right:
                    dfsLst1.append(node.right)
                if node.left:
                    dfsLst1.append(node.left)
                if not node.left and not node.right:lst1.append(node.val)
            return lst1
        if dfsLst(root1)==dfsLst(root2):return True
        else:return False
    def xorQueries(self, arr, queries):
        length=len(arr)
        rtlst=[0]*len(queries)
        Dic=collections.defaultdict(list)
        for i in range(len(queries)):
            Dic[queries[i][0]].append([queries[i][1],i])
        for key in Dic.keys():
            Dic[key]=sorted(Dic[key],key=lambda x:x[0])
        for key in Dic.keys():
            s,ptr=0,0
            i=key
            while ptr<len(Dic[key]) and i<length:
                s^=arr[i]
                while ptr<len(Dic[key]) and i<length and i==Dic[key][ptr][0]:
                    rtlst[Dic[key][ptr][1]]=s
                    ptr+=1
                i+=1
        return rtlst

    def intToRoman(self,num):
        CONVERT={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        if num in CONVERT.keys():
            return CONVERT[num]
        keys=list(CONVERT.keys())
        keys.reverse()
        s=""
        while num:
            for i in keys:
                if num>=i:
                    s+=CONVERT[i]
                    num-=i
                    break
        return s
        

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]
so=Solution()

print(so.xorQueries(arr,queries))
#输出：[8,0,4,4]
#wall=[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]

