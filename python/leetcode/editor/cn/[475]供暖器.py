# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。 
# 
#  在加热器的加热半径范围内的每个房屋都可以获得供暖。 
# 
#  现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。 
# 
#  说明：所有供暖器都遵循你的半径标准，加热的半径也一样。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: houses = [1,2,3], heaters = [2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
#  
# 
#  示例 2: 
# 
#  
# 输入: houses = [1,2,3,4], heaters = [1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
#  
# 
#  示例 3： 
# 
#  
# 输入：houses = [1,5], heaters = [2]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= houses.length, heaters.length <= 3 * 10⁴ 
#  1 <= houses[i], heaters[i] <= 10⁹ 
#  
#  Related Topics 数组 双指针 二分查找 排序 👍 265 👎 0


from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        max_distance = 0
        len_heaters = len(heaters)
        pre_left = 0
        pre_right = min(pre_left + 1, len_heaters - 1)  # pre_right-pre_left<=1
        pre_house = None
        for house in houses:
            if house == pre_house: continue
            pre_house = house
            # 如果在left前
            if house - heaters[pre_left] < 0:
                max_distance = max(max_distance, abs(house - heaters[pre_left]))
            # 如果在左右之间
            elif heaters[pre_right] >= house >= heaters[pre_left]:
                max_distance = max(max_distance, min(abs(house - heaters[pre_left]), abs(house - heaters[pre_right])))
            # 如果在右侧
            elif house - heaters[pre_right] > 0:
                # 如果已经到头
                if pre_right == len_heaters - 1:
                    max_distance = max(max_distance, abs(house - heaters[pre_right]))
                # 如果只用前进一格
                elif heaters[pre_right + 1] >= house >= heaters[pre_left + 1]:
                    pre_left += 1
                    pre_right += 1
                    max_distance = max(max_distance,
                                       min(abs(house - heaters[pre_left]), abs(house - heaters[pre_right])))
                # 二分查找最靠近的两个heater, house在left右侧
                else:
                    left = pre_left
                    right = len_heaters - 1
                    while left <= right:
                        mid = left + ((right - left) >> 1)
                        if heaters[mid] == house:
                            left = mid
                            right = min(mid + 1, len_heaters - 1)
                            break
                        elif heaters[mid] > house:
                            if mid - 1 >= pre_left and heaters[mid - 1] <= house:
                                left = mid - 1
                                right = mid
                                break
                            right = mid
                        else:
                            if mid + 1 < len_heaters and heaters[mid + 1] >= house:
                                left = mid
                                right = mid + 1
                                break
                            left = mid+1
                        pre_left,pre_right=min(left,right),min(right,len_heaters)
                    max_distance = max(max_distance,
                                       min(abs(house - heaters[pre_left]), abs(house - heaters[pre_right])))
        return max_distance


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
print(so.findRadius(houses, heaters))
