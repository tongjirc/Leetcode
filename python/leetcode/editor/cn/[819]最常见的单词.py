# 给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。 
# 
#  题目保证至少有一个词不在禁用列表中，而且答案唯一。 
# 
#  禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。 
# 
#  
# 
#  示例： 
# 
#  输入: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# 输出: "ball"
# 解释: 
# "hit" 出现了3次，但它是一个禁用的单词。
# "ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。 
# 注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 "ball,"）， 
# "hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= 段落长度 <= 1000 
#  0 <= 禁用单词个数 <= 100 
#  1 <= 禁用单词长度 <= 10 
#  答案是唯一的, 且都是小写字母 (即使在 paragraph 里是大写的，即使是一些特定的名词，答案都是小写的。) 
#  paragraph 只包含字母、空格和下列标点符号!?',;. 
#  不存在没有连字符或者带有连字符的单词。 
#  单词里只包含字母，不会出现省略号或者其他标点符号。 
#  
#  Related Topics 哈希表 字符串 计数 👍 128 👎 0


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
import collections
import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count = collections.Counter(re.split("[!?,;. ']", paragraph.lower()))
        sorted_words = sorted(count.keys(),key = lambda x:-count[x])
        for word in sorted_words or word == '':
            if word in banned:
                continue
            else:
                return word

# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(so.mostCommonWord(paragraph, banned))
    print('ball')


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
