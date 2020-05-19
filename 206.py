# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:32:09 2020

@author: AlvinChen
"""
class Solution:
    def reverseList(self, head):
        """
        input type: ListNode
        output type: ListNode
        """
        root=ListNode(0)
        pre=root
        lst=[]
        while head.next:
            lst.append(head.val)
            head=head.next
        lst.append(head.val)
        while lst:
            pre.next=ListNode(lst.pop())
            pre=pre.next
        return root.next

if __name__=="__main__":
    try:
        a=Solution()
        x,n= eval(input()),eval(input())
        print(a.myPow(x,n))
    except Exception as e:
        print(e)