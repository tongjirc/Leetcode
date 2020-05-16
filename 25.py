# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:23:42 2020

@author: AlvinChen
"""
class Solution:
    def reverseKGroup(self, root, k):
        """
        input:
            head:ListNode
            k: int
        output:
            RevLst:ListNode
        """
        if not k:return root
        newhead=None
        newtail=None
        while True:
            head=root
            lst=[None]*k
            for i in range(k):
                lst[i]=root
                print(root.val)
                if not root.next:
                    newhead=head
                    newtail=root
                    break
                root=root.next
            else:
                newhead=lst.pop()
                foo=newhead
                for i in range(1,k-1):
                    foo.next=lst.pop()
                    foo=foo.next
                newtail=foo
            newtail.next=newhead
            if root.next:root=root.next
            else:return newhead

class Solution1:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next


if __name__=="__main__":
    s=Solution()
    steps=eval(input())
    print(s.canJump(steps))