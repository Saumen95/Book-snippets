from pyparsing import Empty


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self.data)

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.isEmpty():
            raise Empty('stack empty')

        return self._data[-1]

    def pop(self):
        if self.isEmpty():
            return self

        return self._data.pop()
