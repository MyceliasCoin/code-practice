# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)
# For example, the binary tree [1,2,2,3,4,4,3] is symmetric:


# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# original solution
class Solution:

    def is_symmetric(self, root: Node) -> bool:

        ans = []

        def helper(root, level):
            if not root:
                return
            else:
                helper(root.left, level + 1)
                ans.append(str(root.val) + '#' + str(level))
                helper(root.right, level + 1)

        helper(root, 0)

        print(ans)

        return all(ans[i] == ans[~i] for i in range(len(ans)//2))


class Solution:

    def is_symmetric(self, root: Node) -> bool:

        ans = []

        self.helper(root, 0, ans)

        print(ans)

        return all(ans[i] == ans[~i] for i in range(len(ans) // 2))

    def helper(self, root, level, answer):

        if not root:
            return

        else:
            self.helper(root.left, level + 1, answer)
            answer.append(str(root.val) + '#' + str(level))
            self.helper(root.right, level + 1, answer)


# driver script
if __name__ == "__main__":

    # create binary tree [1,2,2,3,4,4,3]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    # run solution
    solution = Solution()
    print(solution.is_symmetric(root))
