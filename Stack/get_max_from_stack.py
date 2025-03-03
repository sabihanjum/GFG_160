"""Given q queries, You task is to implement the following three functions for a stack:

push(x) – Insert an integer x onto the stack.
pop() – Remove the top element from the stack.
peek() - Return the top element from the stack. If the stack is empty, return -1.
getMax() – Retrieve the maximum element from the stack in O(1) time. If the stack is empty, return -1.
Each query can be one of the following:

1 x : Push x onto the stack.
2 : Pop the top element from the stack.
3: Return the top element from the stack. If the stack is empty, return -1.
4: Return the maximum element from the stack."""

class MaxStack:
    def __init__(self):
        self.s = []
        self.maxEle = -1

    # Add an element to the top of Stack
    def push(self, x):
        if not self.s:
            self.maxEle = x
            self.s.append(x)
        # If new number is greater than maxEle
        elif x > self.maxEle:
            self.s.append(2 * x - self.maxEle)
            self.maxEle = x
        else:
            self.s.append(x)

    # Remove the top element from the Stack
    def pop(self):
        if not self.s:
            return

        top = self.s.pop()

        # Maximum will change if the maximum element
        # of the stack is being removed.
        if top > self.maxEle:
            self.maxEle = 2 * self.maxEle - top

    # Returns top element of the Stack
    def peek(self):
        if not self.s:
            return -1

        top = self.s[-1]

        # If maxEle < top means maxEle stores value of top.
        return self.maxEle if self.maxEle < top else top

    # Finds maximum element of Stack
    def getMax(self):
        if not self.s:
            return -1

        # variable maxEle stores the maximum element
        # in the stack
        return self.maxEle