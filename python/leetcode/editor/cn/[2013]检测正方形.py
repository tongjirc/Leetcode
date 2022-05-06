# 给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法： 
# 
#  
#  添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。 
#  给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。 
#  
# 
#  轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。 
# 
#  实现 DetectSquares 类： 
# 
#  
#  DetectSquares() 使用空数据结构初始化对象 
#  void add(int[] point) 向数据结构添加一个新的点 point = [x, y] 
#  int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 1
# 0]]]
# 输出：
# [null, null, null, null, 1, 0, null, 2]
# 
# 解释：
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // 返回 1 。你可以选择：
#                                //   - 第一个，第二个，和第三个点
# detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
# detectSquares.add([11, 2]);    // 允许添加重复的点。
# detectSquares.count([11, 10]); // 返回 2 。你可以选择：
#                                //   - 第一个，第二个，和第三个点
#                                //   - 第一个，第三个，和第四个点
#  
# 
#  
# 
#  提示： 
# 
#  
#  point.length == 2 
#  0 <= x, y <= 1000 
#  调用 add 和 count 的 总次数 最多为 5000 
#  
#  Related Topics 设计 数组 哈希表 计数 👍 78 👎 0


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


from functools import reduce
from itertools import product
# leetcode submit region begin(Prohibit modification and deletion)
import collections


class DetectSquares(object):

    def __init__(self):
        self.dct_row_lst = collections.defaultdict(list)
        self.dct_col_lst = collections.defaultdict(list)
        self.dct_square_point = collections.defaultdict(int)  # string("row_columns"):num_of_squares

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        # find avilable suqare point
        # as the edge point
        if point[0] in self.dct_row_lst:
            # make rectangle with same row point
            for point_y in self.dct_row_lst[point[0]]:
                distance = abs(point[1] - point_y)
                point_x = point[0] + distance
                if 0 <= point_x <= 1000 and self.dct_col_lst[point_y].count(point_x) > 0:
                    self.dct_square_point[str(point_x) + "_" + str(point[1])] += self.dct_col_lst[point_y].count(
                        point_x)
                point_x = point[0] - distance
                if 0 <= point_x <= 1000 and self.dct_col_lst[point_y].count(point_x) > 0:
                    self.dct_square_point[str(point_x) + "_" + str(point[1])] += self.dct_col_lst[point_y].count(
                        point_x)
        if point[1] in self.dct_col_lst:
            for point_x in self.dct_col_lst[point[1]]:
                distance = abs(point[0] - point_x)
                point_y = point[1] + distance
                if 0 <= point_y <= 1000 and self.dct_row_lst[point_x].count(point_y) > 0:
                    self.dct_square_point[str(point[0]) + "_" + str(point_y)] += self.dct_row_lst[point_x].count(
                        point_y)
                point_y = point[1] - distance
                if 0 <= point_y <= 1000 and self.dct_row_lst[point_x].count(point_y) > 0:
                    self.dct_square_point[str(point[0]) + "_" + str(point_y)] += self.dct_row_lst[point_x].count(
                        point_y)
        # as the corner point
        if point[0] in self.dct_row_lst and point[1] in self.dct_col_lst:
            dct_abs_dis_y = collections.defaultdict(int)
            for point_y in self.dct_row_lst[point[0]]:
                dct_abs_dis_y[point[1] - point_y] += 1
            for point_x in self.dct_col_lst[point[1]]:
                distance = point[0] - point_x
                if distance in dct_abs_dis_y:
                    self.dct_square_point[str(point_x) + "_" + str(point[1] - distance)] += dct_abs_dis_y[distance]
                if -distance in dct_abs_dis_y:
                    self.dct_square_point[str(point_x) + "_" + str(point[1] + distance)] += dct_abs_dis_y[distance]

        # add point to the dct
        self.dct_row_lst[point[0]].append(point[1])
        self.dct_col_lst[point[1]].append(point[0])

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        return self.dct_square_point[str(point[0]) + "_" + str(point[1])]


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
