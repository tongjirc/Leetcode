# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:47:24 2020

@author: AlvinChen
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        "fast slow pointer"
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__=="__main__":
	s=Solution()
	words=eval(input())
	print(s.middleNode(words))
