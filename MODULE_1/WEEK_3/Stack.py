"""
    Define the Stack class.
"""

from datetime import datetime

class MyStack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._items = []

    def is_empty(self):
        return (len(self._items) == 0)

    def is_full(self):
        return (len(self._items) == self._capacity)
        
    def pop(self):
        popped = self._items.pop()
        return popped
    
    def push(self, value):
        self._items.append(value)
        
    def top(self):
        return self._items[-1]    

def main():
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())

if __name__ == "__main__":
    main()
