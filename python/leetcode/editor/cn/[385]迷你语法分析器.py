# 给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。 
# 
#  列表中的每个元素只可能是整数或整数嵌套列表 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "324",
# 输出：324
# 解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "[123,[456,[789]]]",
# 输出：[123,[456,[789]]]
# 解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
# 1. 一个 integer 包含值 123
# 2. 一个包含两个元素的嵌套列表：
#     i.  一个 integer 包含值 456
#     ii. 一个包含一个元素的嵌套列表
#          a. 一个 integer 包含值 789
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  s 由数字、方括号 "[]"、负号 '-' 、逗号 ','组成 
#  用例保证 s 是可解析的 NestedInteger 
#  输入中的所有值的范围是 [-10⁶, 10⁶] 
#  
#  Related Topics 栈 深度优先搜索 字符串 👍 99 👎 0


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
    def __init__(self):
        self.id = None
        self.left = None
        self.right = None


import time
from functools import reduce
from itertools import product
from memory_profiler import profile


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

# class NestedInteger(object):
#     def __init__(self, value=None):
#         """
#         If value is not specified, initializes an empty list.
#         Otherwise initializes a single integer equal to value.
#         """
#
#     def isInteger(self):
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         :rtype bool
#         """
#
#     def add(self, elem):
#         """
#         Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#         :rtype void
#         """
#
#     def setInteger(self, value):
#         """
#         Set this NestedInteger to hold a single integer equal to value.
#         :rtype void
#         """
#
#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """
#
#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """


class Solution:
    def deserialize(self, s):
        index = 0

        def dfs():
            nonlocal index
            if s[index] == '[':
                index += 1
                ni = NestedInteger()
                while s[index] != ']':
                    ni.add(dfs())
                    if s[index] == ',':
                        index += 1
                index += 1
                return ni
            else:
                negative = False
                if s[index] == '-':
                    negative = True
                    index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    num *= 10
                    num += int(s[index])
                    index += 1
                if negative:
                    num = -num
                return NestedInteger(num)

        return dfs()


# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    s = "[123,[456,[789]]]"


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
