# 我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字
# 母写到下一行。我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...
# ， widths[25] 代表 'z' 需要的单位。 
# 
#  现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。 
# 
#  
# 示例 1:
# 输入: 
# widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10
# ,10,10,10]
# S = "abcdefghijklmnopqrstuvwxyz"
# 输出: [3, 60]
# 解释: 
# 所有的字符拥有相同的占用单位10。所以书写所有的26个字母，
# 我们需要2个整行和占用60个单位的一行。
#  
# 
#  
# 示例 2:
# 输入: 
# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,
# 10,10,10]
# S = "bbbcccdddaaa"
# 输出: [2, 4]
# 解释: 
# 除去字母'a'所有的字符都是相同的单位10，并且字符串 "bbbcccdddaa" 将会覆盖 9 * 10 + 2 * 4 = 98 个单位.
# 最后一个字母 'a' 将会被写到第二行，因为第一行只剩下2个单位了。
# 所以，这个答案是2行，第二行有4个单位宽度。
#  
# 
#  
# 
#  注: 
# 
#  
#  字符串 S 的长度在 [1, 1000] 的范围。 
#  S 只包含小写字母。 
#  widths 是长度为 26的数组。 
#  widths[i] 值的范围在 [2, 10]。 
#  
#  Related Topics 数组 字符串 👍 103 👎 0


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
class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = 1
        begin = 0
        ord_begin = ord('a')
        for chr in s:
            ind = ord(chr) - ord_begin
            if begin + widths[ind] > 100:
                n += 1
                begin = 0
                begin += widths[ind]
            else:
                begin += widths[ind]
        return [n, begin]


# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "bbbcccdddaaa"
    print(so.numberOfLines(widths, s))
    print([2, 4])

    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "abcdefghijklmnopqrstuvwxyz"
    print(so.numberOfLines(widths, s))
    print([3, 60])


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
