class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.array = [None] * k
        self.head = -1
        self.tail = -1
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if (self.isEmpty()):
            self.head = 0
            self.tail = 0
        elif (self.isFull()):
            return;
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.array[self.tail] = value

        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if (self.isEmpty()):
            return
        elif (self.head == self.tail):
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity

        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if (self.isEmpty()):
            return -1

        return self.array[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if (self.isEmpty()):
            return -1
        return self.array[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if (self.head == -1 and self.tail == -1):
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.head == ((self.tail + 1) % self.capacity)):
            return True
        return False