class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here - set the size of the queue to be k
        :param k: int
        """
        self.q = [None] * k
        self.len = k
        self.front = 0
        self.rear = 0

    def enqueue(self, value):
        """
        Insert an element into the circular queue and return true if operation is successful
        :param value: int
        :return: bool
        """
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.len
            return True
        else:
            return False

    def dequeue(self):
        """
        Delete an element from circular queue and return true if operation is successful
        :return: bool
        """
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.len
            return True

    def front(self):
        """
        Get front item in queue
        :return: int
        """
        return -1 if self.q[self.front] is None else self.q[self.front]

    def rear(self):
        """
        Get last item in queue
        :return: int
        """
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def is_empty(self):
        """
        Checks whether circular queue is empty or not
        :return: bool
        """
        return self.front == self.rear and self.q[self.front] is None

    def is_full(self):
        """
        Checks whether circular queue is full or not
        :return: bool
        """
        return self.front == self.rear and self.q[self.front] is not None

