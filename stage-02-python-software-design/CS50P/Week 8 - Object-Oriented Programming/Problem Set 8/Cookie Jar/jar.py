class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self._validate_cookie_count(n)

        if self._size + n > self._capacity:
            raise ValueError

        self._size += n

    def withdraw(self, n):
        self._validate_cookie_count(n)

        if n > self._size:
            raise ValueError

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @staticmethod
    def _validate_cookie_count(n):
        if not isinstance(n, int) or isinstance(n, bool) or n < 0:
            raise ValueError
