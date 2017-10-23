class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flattenedList = self.flatten_nested(nestedList)
        self.iter = 0

    def flatten_nested(self, l):
        p = []
        for item in l:
            if item.isInteger():
                p.append(item)
            else:
                nested = item.getList()
                p += self.flatten_nested(nested)
        return p

    def next(self):
        """
        :rtype: int
        """
        item = self.flattenedList[self.iter]
        self.iter += 1
        return item

    def hasNext(self):
        if self.iter < len(self.flattenedList):
            return True
        """
        :rtype: bool
        """


