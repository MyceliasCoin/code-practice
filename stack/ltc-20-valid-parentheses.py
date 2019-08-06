# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution:
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack to keep track of opening brackets
        stack = []

        # dictionary for tracking mappings
        mapping = {")": "(", "}": "{", "]": "["}

        # loop through every bracket character
        for char in s:

            # if character is an enclosing bracket
            if char in mapping:

                # pop topmost element from stack if it is not empty
                # otherwise assign dummy value of "#"
                top_element = stack.pop() if stack else '#'

                # mapping for opening bracket in our hash and the top
                # if element doesn't match, return False
                if mapping[char] != top_element:
                    return False

            else:
                # this is an opening bracket and we push it onto the stack
                stack.append(char)

        # if stack is empty, then we have a valid expression
        return not stack


# driver script
if __name__ == "__main__":

    # initialize bracket string
    brackets = '{[]}'

    # run solution
    solution = Solution()
    print(solution.is_valid(brackets))
