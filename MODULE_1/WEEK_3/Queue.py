"""
    Define the Queue class.
"""


class MyQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._items = []

    def is_empty(self):
        return (len(self._items) == 0)

    def is_full(self):
        return (len(self._items) == self._capacity)

    def dequeue(self):
        dequeued = self._items.pop(0)
        return dequeued

    def enqueue(self, value):
        self._items.append(value)

    def front(self):
        return self._items[0]


def main():
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())


if __name__ == "__main__":
    main()
