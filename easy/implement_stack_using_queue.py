class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.move()
        return self.queue2.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        self.move()
        return self.queue2[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1

    def move(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
