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


class RouteTree:
    def __init__(self,val):
        self.val=val
        self.trans=[]

def Lst2ListNode(Lst):
    dummy=ListNode(-1,None)
    rcd=dummy
    for i in Lst:
        nd=ListNode(i,None)
        dummy.next=nd
        dummy=dummy.next
    return rcd.next

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

class TreeNode:
    def __init__(self):
        self.id=None
        self.left=None
        self.right=None

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

    def kthLargestValue(self, matrix, k):
        maxk=[]

        def addK(s):
            lenMaxk=len(maxk)
            if lenMaxk==k and s>maxk[-1]:maxk.pop()
            elif lenMaxk==k and s<=maxk[-1]:return
            maxk.append(s)
            for i in range(lenMaxk-2,-1,-1):
                if maxk[i]<maxk[i+1]:maxk[i],maxk[i+1]=maxk[i+1],maxk[i]
                else:break
            return

        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                s=matrix[i][j]
                if i-1>=0:s^=matrix[i-1][j]
                if j-1>=0:s^=matrix[i][j-1]
                if i-1>=0 and j-1>=0:s^matrix[i-1][j-1]
                matrix[i][j]=s
                addK(s)
        return maxk[k-1]

    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

    def openLock(self, deadends, target):
        searchingLst=[["0000",0]]
        searchedLst=set()
        deadends=set(deadends)
        if "0000" in deadends:return -1
        while searchingLst:
            point,depth=searchingLst.pop(0)
            if point==target:return depth
            if point in searchedLst:continue
            searchedLst.add(point)
            for x,y,z,w in [[1,0,0,0],[-1,0,0,0],[0,1,0,0],[0,-1,0,0],[0,0,1,0],[0,0,-1,0],[0,0,0,1],[0,0,0,-1]]:
                newPoint=str((int(point[0])+x)%10)+str((int(point[1])+y)%10)+str((int(point[2])+z)%10)+str((int(point[3])+w)%10)
                if newPoint in searchedLst or newPoint in deadends :continue
                else:
                    searchingLst.append([newPoint,depth+1])
                    for i in range(len(searchingLst)-1,0,-1):
                        if searchingLst[i][1]<searchingLst[i-1][1]:
                            searchingLst[i],searchingLst[i-1]=searchingLst[i-1],searchingLst[i]
                        else:
                            break
        return -1
    def isNumber(self, s):
        #None
        s=s.strip(" ")
        if not s:return False

        #Int
        def isInt(s):
            if s[0]=="+" or s[0]=="-":s=s[1:]
            if not s:return False
            for i in s:
                if not "0"<=i<="9":return False
            return True

        #Double
        def isDouble(s):
            if s[0]=="+" or s[0]=="-":s=s[1:]
            intLst=s.split('.')
            if len(intLst)>2:return False
            numCount=0
            for i in intLst:
                if not i:continue
                if not "0"<=i[0]<="9" or not isInt(i):return False
                numCount+=1
            return True if numCount>=1 else False

        #E or e
        def isE(s):
            numLst=[]
            if "e" in s:numLst=s.split('e')
            elif "E" in s:numLst=s.split('E')
            else:return False
            if len(numLst)!=2:return False
            for i in numLst:
                if not i:return False
            if not isDouble(numLst[0]) and not isInt(numLst[0]):return False
            if not isInt(numLst[1]):return False
            return True

        return isInt(s) or isDouble(s) or isE(s)
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        numPub=len(routes)
        sourceRoute=[i for i in range(numPub) if source in routes[i]]
        targetRoute=[i for i in range(numPub) if target in routes[i]]
        routeLst=[RouteTree(i) for i in range(numPub)]
        for route in routeLst:
            for pt in routes[route.val]:
                for routeNum in range(numPub):
                    if routeNum==route.val:continue
                    if pt in routes[routeNum]:route.trans.append(routeNum)

        def FindMinPath(sPt,tPt,mindepth):
            foundLst=[0]*numPub
            bfsLst=[[routeLst[sPt],1]]
            while bfsLst:
                nd,depth=bfsLst.pop(0)
                if depth>numPub or depth>mindepth:return float("inf")
                if nd.val==tPt:return depth
                for r in nd.trans:
                    if foundLst[r]==1:continue
                    bfsLst.append([routeLst[r],depth+1])

        minPub=float("inf")
        for sourcePt in sourceRoute:
            for targetPt in targetRoute:
                n=FindMinPath(sourcePt,targetPt,minPub)
                minPub=min(minPub,n)
        return minPub if minPub!=float("inf") else -1

    def restoreArray(self, adjacentPairs):
        if not len(adjacentPairs) or not len(adjacentPairs[0]):return []
        l1=len(adjacentPairs)
        NodeDic=collections.defaultdict(TreeNode)
        NotFullNodeDic=collections.defaultdict(TreeNode)
        for i in range(l1):
            x,y=adjacentPairs[i]
            ndx=NotFullNodeDic[x]
            ndx.id=x
            ndy=NotFullNodeDic[y]
            ndy.id=y
            if ndx.left==None:
                ndx.left=ndy
            else:
                ndx.right=ndy
                NodeDic[x]=ndx
                NotFullNodeDic.pop(x)
            if ndy.left==None:
                ndy.left=ndx
            else:
                ndy.right=ndx
                NodeDic[y]=ndy
                NotFullNodeDic.pop(y)
        left,right=NotFullNodeDic.values()
        rtLst=[]
        while left.left or left.right:
            rtLst.append(left.id)
            tmp=left
            if left.left:left=left.left
            elif left.right:left=left.right
            else:break
            if left.left==tmp:left.left=None
            else:left.right=None
        rtLst.append(right.id)
        return rtLst

adjacentPairs = [[2,1],[3,4],[3,2]]
so=Solution()
print(so.restoreArray(adjacentPairs))

#示例 1：
#
#输入：arr = [0,1,0]
#输出：1
#示例 2：
#
#输入：arr = [0,2,1,0]
#输出：1
#示例 3：
#
#输入：arr = [0,10,5,2]
#输出：1
#示例 4：
#
#输入：arr = [3,4,5,1]
#输出：2
#示例 5：
#
#输入：arr = [24,69,100,99,79,78,67,36,26,19]
#输出：2
#
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
