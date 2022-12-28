class Solution:

    # Day 1 p1
    #     def runningSum(self, nums: list[int]) -> list[int]:
    #         total_list = []
    #         for i in range(len(nums)):
    #             # add nums from 0 to current i + 1
    #             total = sum(nums[:i + 1])
    #             total_list.append(total)
    #         return total_list

    #  after watching java solution came up with python way
    def runningSum(self, nums: list[int]) -> list[int]:
        total_list = [nums[0]]  # this syntax is new to me!  initialize list and set item
        for i in range(1, len(nums)):
            total = nums[i] + total_list[i - 1]
            total_list.append(total)
        return total_list

    # faster code by other user - review
    # def runningSum(self, nums: List[int]) -> List[int]:
    #     for i in range(1, len(nums)):
    #         nums[i] += nums[i - 1]
    #     return nums

    # Day 1 p2 - my code
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            # sets total to 0 if we are on left bound
            if i == 0:
                first_half = 0
            else:
                first_half = sum(nums[:i])
            second_half = sum(nums[i + 1:])
            # print test
            print(f"{first_half} vs {second_half}")
            if first_half == second_half:
                return i
        # if not found at end of for loop returns -1
        return -1

    # faster code by other user - review
    # at each index, you need to find left sum and right sum
    # if equivalent, return index
    # else keep going. if you don't find it return -1
    # def pivotIndex(self, nums: list[int]) -> int:
    #     left, right = 0, sum(nums)
    #     for index, num in enumerate(nums):
    #         right -= num
    #         if right == left:
    #             return index
    #         left += num
    #     return -1
