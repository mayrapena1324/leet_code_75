# Source : https://leetcode.com/problems/running-sum-of-1d-array/
# ********************************************************************************** #
"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""


# **********************************************************************************
class Solution:
    #  after watching java solution came up with python way. Earlier solutions below
    def runningSum(self, nums: list[int]) -> list[int]:
        total_list = [nums[0]]  # this syntax is new to me!  initialize list and set item
        for i in range(1, len(nums)):
            total = nums[i] + total_list[i - 1]
            total_list.append(total)
        return total_list

#     def runningSum(self, nums: list[int]) -> list[int]:
#         total_list = []
#         for i in range(len(nums)):
#             # add nums from 0 to current i + 1
#             total = sum(nums[:i + 1])
#             total_list.append(total)
#         return total_list

# # faster code by other user - review
#     def runningSum(self, nums: list[int]) -> list[int]:
#         for i in range(1, len(nums)):
#             nums[i] += nums[i - 1]
#         return nums
