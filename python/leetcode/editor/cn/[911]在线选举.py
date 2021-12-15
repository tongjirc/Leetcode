# 给你两个整数数组 persons 和 times 。在选举中，第 i 张票是在时刻为 times[i] 时投给候选人 persons[i] 的。 
# 
#  对于发生在时刻 t 的每个查询，需要找出在 t 时刻在选举中领先的候选人的编号。 
# 
#  在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。 
# 
#  实现 TopVotedCandidate 类： 
# 
#  
#  TopVotedCandidate(int[] persons, int[] times) 使用 persons 和 times 数组初始化对象。 
#  int q(int t) 根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。 
#  
#  
# 
#  示例： 
# 
#  
# 输入：
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
# [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [
# 24], [8]]
# 输出：
# [null, 0, 1, 1, 0, 0, 1]
# 
# 解释：
# TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1,
#  0], [0, 5, 10, 15, 20, 25, 30]);
# topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
# topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
# topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在
# 平局的情况下，1 是最近获得投票的候选人）。
# topVotedCandidate.q(15); // 返回 0
# topVotedCandidate.q(24); // 返回 0
# topVotedCandidate.q(8); // 返回 1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= persons.length <= 5000 
#  times.length == persons.length 
#  0 <= persons[i] < persons.length 
#  0 <= times[i] <= 10⁹ 
#  times 是一个严格递增的有序数组 
#  times[0] <= t <= 10⁹ 
#  每个测试用例最多调用 10⁴ 次 q 
#  
#  Related Topics 设计 数组 哈希表 二分查找 👍 64 👎 0


from functools import reduce
from itertools import product

# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, OrderedDict
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        person_score = defaultdict(int)  # {person:score}
        winner = [None, 0]
        self.time_win = []
        for i in range(1, len(persons) + 1):
            person_score[persons[i - 1]] += 1
            if person_score[persons[i - 1]] >= winner[1]:
                winner = [persons[i - 1], person_score[persons[i - 1]]]
            self.time_win.append([times[i - 1], winner[0]])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        left, right = 0,len(self.time_win)-1
        if t>=self.time_win[right][0]:
            return self.time_win[right][1]
        elif t<=self.time_win[left][0]:
            return self.time_win[left][1]
        else:
            while left<=right:
                mid=left+((right-left)>>1)
                if self.time_win[mid][0]==t:
                    return self.time_win[mid][1]
                elif self.time_win[mid][0]>t:
                    if self.time_win[mid-1][0]<=t:
                        return self.time_win[mid-1][1]
                    right=mid
                else:
                    if self.time_win[mid+1][0]>t:
                        return self.time_win[mid][1]
                    left=mid+1
            return None

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# leetcode submit region end(Prohibit modification and deletion)
times = [0, 5, 10, 15, 20, 25, 30]
persons = [0, 1, 1, 0, 0, 1, 0]

so = TopVotedCandidate(persons, times)
for i in [[3], [12], [25], [15], [24], [8]]:
    print(i, so.q(i))
