# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution:
    def cal_points(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # stack to keep track of opening brackets
        stack = []

        # use append and pop operations on stack for each operation
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)


# driver script
if __name__ == "__main__":

    # initialize bracket string
    brackets1 = ["5", "2", "C", "D", "+"]
    brackets2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]

    # run solution
    solution = Solution()
    print(solution.cal_points(brackets1))
    print(solution.cal_points(brackets2))
