# 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。. 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树的节点数在 [0, 5000] 范围内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 排序 👍 97 👎 0


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
    while node:
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
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def LNR(self):
        dfs_lst = [self]
        while dfs_lst:
            node = dfs_lst.pop()
            if node.left is not None:
                left = node.left
                node.left = None
                dfs_lst.append(node)
                dfs_lst.append(left)
            elif node.val is not None:
                tmp = node.val
                node.val = None
                dfs_lst.append(node)
                yield tmp
            elif node.right is not None:
                dfs_lst.append(node.right)
                node.right = None
        yield None


import time
from functools import reduce
from itertools import product
from memory_profiler import profile


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def dfs_yield(root):
            if root is None:
                yield None
            dfs_lst = [root]
            while dfs_lst:
                node = dfs_lst.pop()
                if node.left is not None:
                    left = node.left
                    node.left = None
                    dfs_lst.append(node)
                    dfs_lst.append(left)
                elif node.val is not None:
                    tmp = node.val
                    node.val = None
                    dfs_lst.append(node)
                    yield tmp
                elif node.right is not None:
                    dfs_lst.append(node.right)
                    node.right = None
            yield None

        rt_lst = []
        if root1 is None and root2 is None:
            return rt_lst
        itr_left = dfs_yield(root1)
        itr_right = dfs_yield(root2)
        left,right = next(itr_left), next(itr_right)
        while left is not None or right is not None:
            if left is None or right is None:
                if left is not None:
                    rt_lst.append(left)
                    left = next(itr_left)
                else:
                    rt_lst.append(right)
                    right = next(itr_right)
            else:
                if left > right:
                    rt_lst.append(right)
                    right = next(itr_right)
                else:
                    rt_lst.append(left)
                    left = next(itr_left)
        return rt_lst



# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()


@profile(precision=8)
def speed_memory_test():
    print("\nSpeed and memory test")
    start = time.time()
    so = Solution()
    for _ in range(10000):
        pass
    print("Spend time:" + str(int((time.time() - start) * 1000)) + "ms")


# end test

def test():
    precesion_test()
    speed_memory_test()


if __name__ == "__main__":
    test()
