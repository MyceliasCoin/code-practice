# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2
# If it does not exist, output -1 for this number


class Solution:
    def next_greater_element(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # stack to keep track of opening brackets
        stack = []

        # dictionary for tracking mappings
        unordered_map = {}

        for i in nums2:
            while stack and i > stack[-1]:
                unordered_map[stack[-1]] = i
                stack.pop()
            stack.append(i)

        res = []

        for j in nums1:
            if j in unordered_map:
                res.append(unordered_map[j])
            else:
                res.append(-1)

        return res


# driver script
if __name__ == "__main__":

    # initialize bracket string
    parent = [1, 5, 2, 4, 3]
    child = [5, 2]

    # run solution
    solution = Solution()
    print(solution.next_greater_element(child, parent))
