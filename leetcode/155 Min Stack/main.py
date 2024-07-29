"""
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.

"""

"""
    SOLUTIONS OBSERVATIONS
    two stacks, one for keeping the stack and other to keep the current minimum of the stack
    solution is O(1) for time complexity
    and O(n) for space complexity
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minimumStack:
            self.minimumStack.append(val)
        elif self.minimumStack[-1] < val:
            self.minimumStack.append(self.minimumStack[-1])
        else:
            self.minimumStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push()
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
minStack.top()    # return 0
minStack.getMin() # return -2
