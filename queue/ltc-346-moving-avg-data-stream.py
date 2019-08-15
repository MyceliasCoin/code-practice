class Solution:

    def __init__(self, size):
        """
        Initialize your data structure here
        :param size: int
        """
        self.lst = []
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        add new value to queue and calculate moving average
        :param val: int
        :return: float
        """
        # if queue length is equal to max size of queue, decrement sum and pop from queue
        if len(self.lst) >= self.size:
            self.sum -= self.lst.pop(0)

        # append new value to queue and increment sum
        self.lst.append(val)
        self.sum += val

        # return queue average
        return self.sum / len(self.lst)


# driver script
if __name__ == "__main__":

    # run solution
    solution = Solution(3)

    # run test cases
    print(solution.next(1))
    print(solution.next(10))
    print(solution.next(3))
    print(solution.next(5))
