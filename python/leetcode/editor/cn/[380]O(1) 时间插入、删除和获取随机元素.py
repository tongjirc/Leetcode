# 实现RandomizedSet 类： 
# 
#  
#  
#  
#  RandomizedSet() 初始化 RandomizedSet 对象 
#  bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。 
#  bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。 
#  int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。 
#  
# 
#  你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。 
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", 
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# 输出
# [null, true, false, true, 2, true, false, 2]
# 
# 解释
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
# randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
# randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
# randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  最多调用 insert、remove 和 getRandom 函数 2 * 10⁵ 次 
#  在调用 getRandom 方法时，数据结构中 至少存在一个 元素。 
#  
#  
#  
#  Related Topics 设计 数组 哈希表 数学 随机化 👍 480 👎 0


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
class RandomizedSet(object):

    def __init__(self):


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """


    def getRandom(self):
        """
        :rtype: int
        """



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
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


