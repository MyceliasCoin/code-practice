# Given an array nums of n integers where n > 1,  return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i].
# Note: please solve it without division and in O(n).
# Follow up: try to also solve in constant space complexity
# Output array does not count as extra space for the purpose of space complexity analysis

#


class Solution1:
    def product_except_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # get length of the input array
        length = len(nums)

        # create empty left and right arrays
        left, right, ans = [0] * length, [0] * length, [0] * length

        # left[i] contains product of all elements to the left of i
        # given there are no elements at the left of index 0, left[0] is just 1
        left[0] = 1

        # loop through and generate left product array
        for i in range(1, length):
            # left[i-1] already contains product of elements to the left of 'i-1'
            # simply multiply it with nums[i-1] to generate left product array
            left[i] = nums[i-1] * left[i-1]

        # right[i] contains the product of all the elements to the right of i
        # given there are no elements to the right of index length - 1, right[length-1= is just 1
        right[length-1] = 1

        # loop through and generate right product array
        for i in reversed(range(length - 1)):
            # right[i+1] already contains product of elements to the right of 'i+1'
            # simply multiply it with nums[i+1] to generate right product array
            right[i] = nums[i+1] * right[i+1]

        # construct the answer array
        for i in range(length):
            # multiply product of all elements from left and right product arrays
            ans[i] = left[i] * right[i]

        return ans


class Solution:
    def product_except_self(self, nums):

        # get length of the input array
        length = len(nums)

        # initialize answer array
        ans = [0] * length

        # ans[i] contains product of all elements to left of i
        # given there are no elements at the left of index 0, ans[0] is just 1
        ans[0] = 1

        # loop through and generate answer array
        for i in range(1, length):
            # ans[i-1] already contains product of elements to the left of 'i-1'
            # simply multiply it with nums[i-1] to give product of all elements to left of i
            ans[i] = nums[i-1] * ans[i-1]

        # right contains product of all elements to the right of i
        # given there are no elements at the right of index 'length - 1', right is just 1
        right = 1

        # loop through reversed array and generate answer array
        for i in reversed(range(length)):
            # for index i, right contains product of all elements to the right
            ans[i] = ans[i] * right
            right *= nums[i]

        return ans


# driver script
if __name__ == "__main__":

    # set inputs and run solution
    nums1 = [1, 2, 3, 4]
    solution = Solution()

    # print result
    print(solution.product_except_self(nums1))
