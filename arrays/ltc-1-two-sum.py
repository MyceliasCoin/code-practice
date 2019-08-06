# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target-nums[i]], i]


# driver script
if __name__ == "__main__":

    # run solution
    solution = Solution()
    print(solution.two_sum([2, 7, 11, 15], 9))
