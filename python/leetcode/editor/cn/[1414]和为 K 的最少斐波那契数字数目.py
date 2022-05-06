# 给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。 
# 
#  斐波那契数字定义为： 
# 
#  
#  F1 = 1 
#  F2 = 1 
#  Fn = Fn-1 + Fn-2 ， 其中 n > 2 。 
#  
# 
#  数据保证对于给定的 k ，一定能找到可行解。 
# 
#  
# 
#  示例 1： 
# 
#  输入：k = 7
# 输出：2 
# 解释：斐波那契数字为：1，1，2，3，5，8，13，……
# 对于 k = 7 ，我们可以得到 2 + 5 = 7 。 
# 
#  示例 2： 
# 
#  输入：k = 10
# 输出：2 
# 解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。
#  
# 
#  示例 3： 
# 
#  输入：k = 19
# 输出：3 
# 解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= 10^9 
#  
#  Related Topics 贪心 👍 133 👎 0


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
from memory_profiler import profile
from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        f = [1, 1]
        while f[-1] < k:
            f.append(f[-1] + f[-2])
        ans, i = 0, len(f) - 1
        while k:
            if k >= f[i]:
                k -= f[i]
                ans += 1
            i -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

from memory_profiler import profile
# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    k = 7
    print(so.findMinFibonacciNumbers(k))
    print(2)

    print(so.findMinFibonacciNumbers(10))
    print(2)

    print(so.findMinFibonacciNumbers(19))
    print(3)

@profile(precision=8)
def speed_memory_test():
    print("\nSpeed and memory test")
    start = time.time()
    so = Solution()
    for _ in range(10000):
        so.findMinFibonacciNumbers(19)
        pass
    print("Spend time:" + str(int((time.time() - start) * 1000)) + "ms")
# end test

def test():
    precesion_test()
    speed_memory_test()

if __name__ == "__main__":
    test()

