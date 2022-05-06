# 给你一支股票价格的数据流。数据流中每一条记录包含一个 时间戳 和该时间点股票对应的 价格 。 
# 
#  不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条
# 记录视为错误记录，后出现的记录 更正 前一条错误的记录。 
# 
#  请你设计一个算法，实现： 
# 
#  
#  更新 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将 更正 之前的错误价格。 
#  找到当前记录里 最新股票价格 。最新股票价格 定义为时间戳最晚的股票价格。 
#  找到当前记录里股票的 最高价格 。 
#  找到当前记录里股票的 最低价格 。 
#  
# 
#  请你实现 StockPrice 类： 
# 
#  
#  StockPrice() 初始化对象，当前无股票价格记录。 
#  void update(int timestamp, int price) 在时间点 timestamp 更新股票价格为 price 。 
#  int current() 返回股票 最新价格 。 
#  int maximum() 返回股票 最高价格 。 
#  int minimum() 返回股票 最低价格 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：
# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", 
# "update", "minimum"]
# [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
# 输出：
# [null, null, null, 5, 10, null, 5, null, 2]
# 
# 解释：
# StockPrice stockPrice = new StockPrice();
# stockPrice.update(1, 10); // 时间戳为 [1] ，对应的股票价格为 [10] 。
# stockPrice.update(2, 5);  // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
# stockPrice.current();     // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
# stockPrice.maximum();     // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
# stockPrice.update(1, 3);  // 之前时间戳为 1 的价格错误，价格更新为 3 。
#                           // 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
# stockPrice.maximum();     // 返回 5 ，更正后最高价格为 5 。
# stockPrice.update(4, 2);  // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
# stockPrice.minimum();     // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= timestamp, price <= 10⁹ 
#  update，current，maximum 和 minimum 总 调用次数不超过 10⁵ 。 
#  current，maximum 和 minimum 被调用时，update 操作 至少 已经被调用过 一次 。 
#  
#  Related Topics 设计 哈希表 数据流 有序集合 堆（优先队列） 👍 31 👎 0


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

from sortedcontainers import SortedDict,SortedList,SortedSet
from functools import reduce
from itertools import product

# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedDict,SortedList,SortedSetrs import SortedDict,SortedList,SortedSet
class StockPrice(object):

    def __init__(self):
        self.dct_timestamp_price = {}
        self.price = SortedList()
        self.current_time = 0


    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if timestamp in self.dct_timestamp_price:
            self.price.discard(self.dct_timestamp_price[timestamp])
        self.dct_timestamp_price[timestamp] = price
        self.price.add(price)
        self.current_time = max(self.current_time, timestamp)
            

    def current(self):
        """
        :rtype: int
        """
        return self.dct_timestamp_price[self.current_time]


    def maximum(self):
        """
        :rtype: int
        """
        return self.price[-1]


    def minimum(self):
        """
        :rtype: int
        """
        return self.price[0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# leetcode submit region end(Prohibit modification and deletion)

so = Solution()