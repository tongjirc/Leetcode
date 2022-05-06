# 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于 n 的 最简 分数 。分数可以以 任意 顺序返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：["1/2"]
# 解释："1/2" 是唯一一个分母小于等于 2 的最简分数。 
# 
#  示例 2： 
# 
#  输入：n = 3
# 输出：["1/2","1/3","2/3"]
#  
# 
#  示例 3： 
# 
#  输入：n = 4
# 输出：["1/2","1/3","1/4","2/3","3/4"]
# 解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。 
# 
#  示例 4： 
# 
#  输入：n = 1
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  
#  Related Topics 数学 字符串 数论 👍 42 👎 0


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
from math import gcd


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for mother in range(2, n + 1):
            ans.append(str(1) + "/" + str(mother))
            for children in range(2, mother):
                if gcd(mother, children) == 1:
                    ans.append(str(children) + "/" + str(mother))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    n = 2
    print(so.simplifiedFractions(n))
    print(["1/2"])

    print(so.simplifiedFractions(3))
    print(["1/2", "1/3", "2/3"])

    print(so.simplifiedFractions(1))
    print([])

    print(so.simplifiedFractions(4))
    print(["1/2", "1/3", "1/4", "2/3", "3/4"])

    print(so.simplifiedFractions(6))
    print(["1/2", "1/3", "1/4", "1/5", "1/6", "2/3", "2/5", "3/4", "3/5", "4/5", "5/6"])


@profile(precision=8)
def speed_memory_test():
    print("\nSpeed and memory test")
    start = time.time()
    so = Solution()
    for _ in range(10000):
        so.simplifiedFractions(3)
        pass
    print("Spend time:" + str(int((time.time() - start) * 1000)) + "ms")


# end test

def test():
    precesion_test()
    speed_memory_test()


if __name__ == "__main__":
    test()
