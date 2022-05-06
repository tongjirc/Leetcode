# 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。 
# 
#  返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的
# 字符 c 的 距离 。 
# 
#  两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "loveleetcode", c = "e"
# 输出：[3,2,1,0,1,0,0,1,2,2,1,0]
# 解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
# 距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
# 距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
# 对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
# 距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aaab", c = "b"
# 输出：[3,2,1,0]
#  
# 
#  
# 提示：
# 
#  
#  1 <= s.length <= 10⁴ 
#  s[i] 和 c 均为小写英文字母 
#  题目数据保证 c 在 s 中至少出现一次 
#  
#  Related Topics 数组 双指针 字符串 👍 272 👎 0
import collections


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
from collections import deque


class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        length = len(s)
        bfslst = deque()
        rt_lst = [-1] * length
        index = s.find(c)
        while index != -1:
            bfslst.append([index, 0])
            index = s.find(c, index + 1)
        while bfslst:
            i, dis = bfslst.popleft()
            if rt_lst[i] == -1:
                rt_lst[i] = dis
                if i - 1 >= 0:
                    bfslst.append([i - 1, dis + 1])
                if i + 1 < length:
                    bfslst.append([i + 1, dis + 1])
        return rt_lst


# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    s = "loveleetcode"
    c = "e"
    print(so.shortestToChar(s, c))
    print([3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])


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
