# 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。 
# 
#  注意： 
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。 
# 
#  示例: 
# 
#  
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
# solution.pick(3);
# 
# // pick(1) 应该返回 0。因为只有nums[0]等于1。
# solution.pick(1);
#  
#  Related Topics 水塘抽样 哈希表 数学 随机化 👍 186 👎 0


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

    def __init__(self, nums):
        """
        :type nums: List[int]
        """


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
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


