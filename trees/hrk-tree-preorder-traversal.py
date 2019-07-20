class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root):
    # Write your code here

    if root:
        print(str(root.info) + " ", end="")
        preOrder(root.left)
        preOrder(root.right)


# driver script
if __name__ == "__main__":

    # create binary tree
    tree = BinarySearchTree()

    # prompt user for array length
    t = int(input())

    # prompt user for values to put into array
    arr = list(map(int, input().split()))

    # loop through array and create tree
    for i in range(t):
        tree.create(arr[i])

    # run
    preOrder(tree.root)

# test case 1
# 6
# 1 2 5 3 6 4

# test case 2
# 15
# 1 14 3 7 4 5 15 6 13 10 11 2 12 8 9
