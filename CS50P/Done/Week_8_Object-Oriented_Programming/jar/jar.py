
class Jar:
    def __init__(self, capacity=12):
        if not (type(capacity) == int and (capacity)>=0):
            raise ValueError("must be an non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not(type(n) == int and (n)>=0):
            raise ValueError("must be an non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Can not deposit more than the capacity")
        self._size = self._size + n


    def withdraw(self, n):
        if not(type(n) == int and (n)>=0):
            raise ValueError("must be an non-negative integer")
        if n > self._size:
            raise ValueError("can not take out more than what is owned")
        self._size = self.size-n
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
