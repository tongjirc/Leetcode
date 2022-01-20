# 给定一个单链表 L 的头节点 head ，单链表 L 表示为： 
# 
#  
# L0 → L1 → … → Ln - 1 → Ln
#  
# 
#  请将其重新排列后变为： 
# 
#  
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → … 
# 
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3] 
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 5 * 10⁴] 
#  1 <= node.val <= 1000 
#  
#  Related Topics 栈 递归 链表 双指针 👍 758 👎 0

def Lst2ListNode(Lst):
    dummy = ListNode(-1, None)
    rcd = dummy
    for i in Lst:
        nd = ListNode(i, None)
        dummy.next = nd
        dummy = dummy.next
    return rcd.next


def ListNode2Lst(node):
    Lst = []
    while node is not None:
        Lst.append(node.val)
        node = node.next
    return Lst


class ListNode(object):
    _name = "ListNode"

    def __init__(self, val=0, next=None, lst=[]):
        if not lst:
            self.val = val
            self.next = next
        else:
            self.val = lst.pop(0)
            if lst:
                self.next = ListNode(lst=lst)
            else:
                self.next = None

    def __str__(self):
        return str(ListNode2Lst(self))


class TreeNode:
    def __init__(self):
        self.id = None
        self.left = None
        self.right = None


from functools import reduce
from itertools import product
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        dummy = ListNode()
        dummy.next = head
        lst_node = []
        while head is not None:
            lst_node.append(head)
            head = head.next
        head = lst_node[0]
        for i in range(1,len(lst_node)):
            head.next = lst_node[i//2] if i % 2 == 0 else lst_node[- i//2 - 1]
            if i % 2 == 0:print(i//2)
            else:print(-i//2 -1)
            head = head.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
head = ListNode(lst=[1, 2, 3, 4])
print(so.reorderList(head))
