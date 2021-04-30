# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:17:23 2020

@author: AlvinChen
"""

class Solution:
    def bubbleSort(self, lst):
        """
        bubble sort
        """
        n=len(lst)
        if n<=1:
            return lst
        for i in range (0,n):
            for j in range(0,n-i-1):
                if lst[j]>lst[j+1]:
                    (lst[j],lst[j+1])=(lst[j+1],lst[j])
        return lst

    def quickSort(self,lst):
        # 此函数完成分区操作
        def partition(arr, left, right):
            key = left  # 划分参考数索引,默认为第一个数为基准数，可优化
            while left < right:
                # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
                while left < right and arr[right] >= arr[key]:
                    right -= 1
                # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
                while left < right and arr[left] <= arr[key]:
                    left += 1
                # 此时已找到一个比基准大的书，和一个比基准小的数，将他们互换位置
                (arr[left], arr[right]) = (arr[right], arr[left])
            # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
            (arr[left], arr[key]) = (arr[key], arr[left])
            # 返回目前基准所在位置的索引
            return left

        def quicksort(arr, left, right):
            if left >= right:
                return
            # 从基准开始分区
            mid = partition(arr, left, right)
            # 递归调用
            # print(arr)
            quicksort(arr, left, mid - 1)
            quicksort(arr, mid + 1, right)

        # 主函数
        n = len(lst)
        if n <= 1:
            return lst
        quicksort(lst, 0, n - 1)
        return lst

    def InsertSort(self,lst):
        n=len(lst)
        if n<=1:
            return lst
        for i in range(1,n):
            j=i
            target=lst[i]            #每次循环的一个待插入的数
            while j>0 and target<lst[j-1]:       #比较、后移，给target腾位置
                lst[j]=lst[j-1]
                j=j-1
            lst[j]=target            #把target插到空位
            return lst

    def ShellSort(self,lst):
        def shellinsert(arr,d):
            n=len(arr)
            for i in range(d,n):
                j=i-d
                temp=arr[i]             #记录要出入的数
                while(j>=0 and arr[j]>temp):    #从后向前，找比其小的数的位置
                    arr[j+d]=arr[j]                 #向后挪动
                    j-=d
                if j!=i-d:
                    arr[j+d]=temp
        n=len(lst)
        if n<=1:
            return lst
        d=n//2
        while d>=1:
            shellinsert(lst,d)
            d=d//2
        return lst

    def SelectSort(self,lst):
        n=len(lst)
        if n<=1:
            return lst
        for i in range(0,n-1):
            minIndex=i
            for j in range(i+1,n):          #比较一遍，记录索引不交换
                if lst[j]<lst[minIndex]:
                    minIndex=j
            if minIndex!=i:                     #按索引交换
                (lst[minIndex],lst[i])=(lst[i],lst[minIndex])
        return lst


    def  HeapSort(self,lst):
        def heapadjust(arr,start,end):  #将以start为根节点的堆调整为大顶堆
            temp=arr[start]
            son=2*start+1
            while son<=end:
                if son<end and arr[son]<arr[son+1]:  #找出左右孩子节点较大的
                    son+=1
                if temp>=arr[son]:       #判断是否为大顶堆
                    break
                arr[start]=arr[son]     #子节点上移
                start=son                     #继续向下比较
                son=2*son+1
            arr[start]=temp             #将原堆顶插入正确位置

        n=len(lst)
        if n<=1:
            return lst
        #建立大顶堆
        root=n//2-1    #最后一个非叶节点（完全二叉树中）
        while(root>=0):
            heapadjust(ls,root,n-1)
            root-=1
        #掐掉堆顶后调整堆
        i=n-1
        while(i>=0):
            (lst[0],lst[i])=(lst[i],lst[0])  #将大顶堆堆顶数放到最后
            heapadjust(lst,0,i-1)    #调整剩余数组成的堆
            i-=1
        return lst

    def MergeSort(self,lst):
        #合并左右子序列函数
        def merge(arr,left,mid,right):
            temp=[]     #中间数组
            i=left          #左段子序列起始
            j=mid+1   #右段子序列起始
            while i<=mid and j<=right:
                if arr[i]<=arr[j]:
                    temp.append(arr[i])
                    i+=1
                else:
                    temp.append(arr[j])
                    j+=1
            while i<=mid:
                temp.append(arr[i])
                i+=1
            while j<=right:
                temp.append(arr[j])
                j+=1
            for i in range(left,right+1):    #  !注意这里，不能直接arr=temp,他俩大小都不一定一样
                arr[i]=temp[i-left]
        #递归调用归并排序
        def mSort(arr,left,right):
            if left>=right:
                return
            mid=(left+right)//2
            mSort(arr,left,mid)
            mSort(arr,mid+1,right)
            merge(arr,left,mid,right)

        n=len(lst)
        if n<=1:
            return lst
        mSort(lst,0,n-1)
        return lst

if __name__=="__main__":
	s=Solution()
	island=eval(input())
	print(s.ShellSort(island))
