# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:12:40 2020

@author: AlvinChen
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(Node1,Node2):
        """
        input: ListNode ListNode
        output:ListNode
        """
        begin=root=ListNode(0) #generate head node to store the head
        while Node1 and Node2:
            if Node1.val>Node2.val:
                root.next=Node2
                Node2=Node2.next
            else:
                root.next=Node1
                Node1=Node1.next
            root=root.next
        if Node1:root.next=Node1
        if Node2:root.next=Node2
        return begin.next


if __name__=="__main__":
    try:
        a=Solution()
        n= eval(input())
        print(a.mergeKLists(n))
    except Exception as e:
        print(e)