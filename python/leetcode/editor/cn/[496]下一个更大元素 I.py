# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。 
# 
#  请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。 
# 
#  nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
#     对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
#     对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。 
# 
#  示例 2: 
# 
#  
# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#     对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
#     对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length <= nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 10⁴ 
#  nums1和nums2中所有整数 互不相同 
#  nums1 中的所有整数同样出现在 nums2 中 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？ 
#  Related Topics 栈 数组 哈希表 单调栈 👍 558 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class PriorityQueue():
    def __init__(self):
        self.queue=[]
    def put(self,num):
        #二分查找
        length=len(self.queue)
        if length==0:
            self.queue.append(num)
            return
        left,right=0,length-1
        if num<self.queue[left]:
            self.queue.insert(0,num)
            return
        elif num>self.queue[right]:
            self.queue.append(num)
            return
        else:
            while left<right:
                mid=left+(right-left)>>1
                if self.queue[mid]>num:
                    if mid>0 and self.queue[mid-1]<num:
                        self.queue.insert(mid,num)
                        return
                    else:
                        right=mid-1
                else:
                    if mid<length-1 and self.queue[mid+1]>num:
                        self.queue.insert(mid+1,num)
                        return
                    else:
                        left=mid
            return right

    def get(self):
        return self.queue.pop(0)
    def empty(self):
        return self.queue==[]

class Solution(object):
    def nextGreaterElement1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_target=set(nums1)
        queue_target=PriorityQueue()
        lst_rt=[-1]*len(nums1)
        for i in nums2:
            while not queue_target.empty():
                target=queue_target.get()
                if target>i:
                    queue_target.put(target)
                    break
                else:
                    lst_rt[nums1.index(target)]=i
            if i in set_target:
                queue_target.put(i)
        return lst_rt

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashSet_target= {}
        monoStack_num2=[]
        lst_ans=[]
        for i in range(len(nums2)-1,-1,-1):
            value=nums2[i]
            #调整单调栈
            while monoStack_num2!=[]:
                if monoStack_num2[-1]<value:
                    monoStack_num2.pop()
                else:
                    break
            if monoStack_num2==[]:
                hashSet_target[value]=-1
            else:
                hashSet_target[value] = monoStack_num2[-1]
            monoStack_num2.append(value)
        for i in nums1:
            lst_ans.append(hashSet_target[i])
        return lst_ans


# leetcode submit region end(Prohibit modification and deletion)
so=Solution()
nums1=[2,4]
nums2=[1,2,3,4]
print(so.nextGreaterElement(nums1,nums2))