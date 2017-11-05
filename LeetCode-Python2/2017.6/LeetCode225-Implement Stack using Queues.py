'''
LeetCode225. Implement Stack using Queues
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''

import collections
import Queue

#【极客学院版】
class MyStackV1(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()
        self.size = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.empty() or not self.queue1.empty():
            self.queue1.put(x)
        else:
            self.queue2.put(x)
        self.size += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        x = 0
        if not self.queue1.empty():
            while self.queue1.qsize() > 1:
                self.queue2.put(self.queue1.get())

            x = self.queue1.get()
        else:
            while self.queue2.qsize() > 1:
                self.queue1.put(self.queue2.get())

            x = self.queue2.get()
        self.size -= 1
        return x

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        x = 0
        if not self.queue1.empty():
            while self.queue1.qsize() > 1:
                self.queue2.put(self.queue1.get())

            x = self.queue1.get()
            self.queue2.put(x)
        else:
            while self.queue2.qsize() > 1:
                self.queue1.put(self.queue2.get())

            x = self.queue2.get()
            self.queue1.put(x)
        return x

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()




class MyStackV2(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        x = self.queue.pop()
        self.queue.append(x)
        return x

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue == self.queue2


        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()