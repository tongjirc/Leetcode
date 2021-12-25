# 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ： 
# 
#  
#  二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。 
#  偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增 
#  奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减 
#  
# 
#  给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# 输出：true
# 解释：每一层的节点值分别是：
# 0 层：[1]
# 1 层：[10,4]
# 2 层：[3,7,9]
# 3 层：[12,8,6,2]
# 由于 0 层和 2 层上的节点值都是奇数且严格递增，而 1 层和 3 层上的节点值都是偶数且严格递减，因此这是一棵奇偶树。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [5,4,2,3,3,7]
# 输出：false
# 解释：每一层的节点值分别是：
# 0 层：[5]
# 1 层：[4,2]
# 2 层：[3,3,7]
# 2 层上的节点值不满足严格递增的条件，所以这不是一棵奇偶树。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [5,9,1,3,5,7]
# 输出：false
# 解释：1 层上的节点值应为偶数。
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1]
# 输出：true
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数在范围 [1, 10⁵] 内 
#  1 <= Node.val <= 10⁶ 
#  
#  Related Topics 树 广度优先搜索 二叉树 👍 30 👎 0

class RouteTree:
    def __init__(self, val):
        self.val = val
        self.trans = []


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
        return str(self.ListNode2Lst(self))

    def ListNode2Lst(self, node):
        Lst = []
        while node:
            Lst.append(node.val)
            node = node.next
        return Lst

    def Lst2ListNode(self, Lst):
        dummy = ListNode(-1, None)
        rcd = dummy
        for i in Lst:
            nd = ListNode(i, None)
            dummy.next = nd
            dummy = dummy.next
        return rcd.next


class TreeNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None


from functools import reduce
from itertools import product
# Definition for a binary tree node.
# leetcode submit region begin(Prohibit modification and deletion)
from queue import deque


class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre_val, pre_depth = float("-inf"), 0
        lst_bfs_node = deque([[root, 0]])
        while lst_bfs_node:
            node, depth = lst_bfs_node.popleft()

            if depth != pre_depth:
                if depth % 2 == 0:
                    pre_val = float("-inf")
                else:
                    pre_val = float("inf")

            if depth % 2 == 0 and node.val > pre_val and node.val % 2 == 1:
                pass
            elif depth % 2 == 1 and node.val < pre_val and node.val % 2 == 0:
                pass
            else:
                return False

            pre_val, pre_depth = node.val, depth
            if node.left: lst_bfs_node.append([node.left, depth + 1])
            if node.right: lst_bfs_node.append([node.right, depth + 1])
        return True


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
root = TreeNode(0)
