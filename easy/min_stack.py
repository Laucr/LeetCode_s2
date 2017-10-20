class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimal = []
        self.data = []
        self.length = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        self.length += 1

        if len(self.minimal) == 0:
            self.minimal.append((x, self.length))

        else:
            if long(x) < long(self.minimal[-1][0]):
                self.minimal.append((x, self.length))

    def pop(self):
        """
        :rtype: void
        """
        if self.length > 0:
            popped = self.data[-1]
            self.data = self.data[:-1]
            if (popped, self.length) == (self.minimal[-1]):
                self.minimal = self.minimal[:-1]
            self.length -= 1

    def top(self):
        """
        :rtype: int
        """
        if self.length > 0:
            return self.data[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minimal) > 0:
            return self.minimal[-1][0]


obj = MinStack()
obj.push(-3)
obj.push(0)
obj.push(-2)
a = obj.getMin()
obj.pop()
b = obj.getMin()
print a, b
