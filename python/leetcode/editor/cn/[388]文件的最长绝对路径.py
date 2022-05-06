# 假设有一个同时存储文件和目录的文件系统。下图展示了文件系统的一个示例： 
# 
#  
# 
#  这里将 dir 作为根目录中的唯一目录。dir 包含两个子目录 subdir1 和 subdir2 。subdir1 包含文件 file1.ext 和子目
# 录 subsubdir1；subdir2 包含子目录 subsubdir2，该子目录下包含文件 file2.ext 。 
# 
#  在文本格式中，如下所示(⟶表示制表符)： 
# 
#  
# dir
# ⟶ subdir1
# ⟶ ⟶ file1.ext
# ⟶ ⟶ subsubdir1
# ⟶ subdir2
# ⟶ ⟶ subsubdir2
# ⟶ ⟶ ⟶ file2.ext
#  
# 
#  如果是代码表示，上面的文件系统可以写为 "dir
# \tsubdir1
# \t\tfile1.ext
# \t\tsubsubdir1
# \tsubdir2
# \t\tsubsubdir2
# \t\t\tfile2.ext" 。'
# ' 和 '\t' 分别是换行符和制表符。 
# 
#  文件系统中的每个文件和文件夹都有一个唯一的 绝对路径 ，即必须打开才能到达文件/目录所在位置的目录顺序，所有路径用 '/' 连接。上面例子中，指向 
# file2.ext 的 绝对路径 是 "dir/subdir2/subsubdir2/file2.ext" 。每个目录名由字母、数字和/或空格组成，每个文件名遵循 
# name.extension 的格式，其中 name 和 extension由字母、数字和/或空格组成。 
# 
#  给定一个以上述格式表示文件系统的字符串 input ，返回文件系统中 指向 文件 的 最长绝对路径 的长度 。 如果系统中没有文件，返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：input = "dir
# \tsubdir1
# \tsubdir2
# \t\tfile.ext"
# 输出：20
# 解释：只有一个文件，绝对路径为 "dir/subdir2/file.ext" ，路径长度 20
#  
# 
#  示例 2： 
# 
#  
# 输入：input = "dir
# \tsubdir1
# \t\tfile1.ext
# \t\tsubsubdir1
# \tsubdir2
# \t\tsubsubdir2
# \t\t\tfile2.ext"
# 输出：32
# 解释：存在两个文件：
# "dir/subdir1/file1.ext" ，路径长度 21
# "dir/subdir2/subsubdir2/file2.ext" ，路径长度 32
# 返回 32 ，因为这是最长的路径 
# 
#  示例 3： 
# 
#  
# 输入：input = "a"
# 输出：0
# 解释：不存在任何文件 
# 
#  示例 4： 
# 
#  
# 输入：input = "file1.txt
# file2.txt
# longfile.txt"
# 输出：12
# 解释：根目录下有 3 个文件。
# 因为根目录中任何东西的绝对路径只是名称本身，所以答案是 "longfile.txt" ，路径长度为 12
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= input.length <= 10⁴ 
#  input 可能包含小写或大写的英文字母，一个换行符 '
# '，一个制表符 '\t'，一个点 '.'，一个空格 ' '，和数字。 
#  
#  Related Topics 栈 深度优先搜索 字符串 👍 141 👎 0


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


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        def get_level(line):
            return line.count("\t")

        def have_file(line):
            return True if line.find('.') != -1 else False

        lst_line = input.split("\n")
        length = len(lst_line)
        if not have_file(input):
            return 0
        lst_bfs = collections.deque()
        # 搜索根目录
        for i in range(length):
            if get_level(lst_line[i]) == 0:
                lst_bfs.append([lst_line[i],i,0])
        max_length_file_path = None
        while lst_bfs:
            abs_file_path, index, level = lst_bfs.popleft()
            if have_file(abs_file_path):
                if max_length_file_path is None or len(abs_file_path) > len(max_length_file_path):
                    max_length_file_path = abs_file_path
            else:
                # 寻找下一级
                for i in range(index + 1, length):
                    now_level = get_level(lst_line[i])
                    if now_level == level + 1:
                        # 下一级
                        lst_bfs.append([abs_file_path + '/' + lst_line[i].strip("\t"), i, level + 1])
                    elif now_level > level + 1:
                        # 下下级
                        continue
                    else:
                        # 同级或上级
                        break
        return len(max_length_file_path) if max_length_file_path is not None else 0


# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(so.lengthLongestPath(input))
    print(32)

    input = "file1.txt\nfile2.txt\nlongfile.txt"
    print(so.lengthLongestPath(input))
    print(12)

    input = "file1.txt"
    print(so.lengthLongestPath(input))
    print(9)

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
