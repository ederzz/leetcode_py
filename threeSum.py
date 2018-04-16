"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.

给定一个n个数字的数组nums,是否存在三个元素a, b, c满足：a + b + c = 0，找到所有这样的组合
注意：
返回值中不能有重复组合.

example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [] # 返回值
    nums.sort() # 排序
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue # 排除重复组合
        l, r = i + 1, len(nums) - 1 # 游标索引
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1 # 排除重复结果
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1 # 排除重复结果
                l += 1; r -= 1
    return res

print(threeSum([-1, 0, 1, 2, -1, -4]))