class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.s.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.s:
            self.s.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.s
