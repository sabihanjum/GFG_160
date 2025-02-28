"""Given q queries, You task is to implement the following four functions for a stack:

push(x) – Insert an integer x onto the stack.
pop() – Remove the top element from the stack.
peek() - Return the top element from the stack. If the stack is empty, return -1.
getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
Each query can be one of the following:

1 x : Push x onto the stack.
2 : Pop the top element from the stack.
3: Return the top element from the stack. If the stack is empty, return -1.
4: Return the minimum element from the stack."""

class SpecialStack:
    def __init__(self):
        self.s = []
        self.minEle = -1

    # Add an element to the top of Stack
    def push(self, x):
        if not self.s:
            self.minEle = x
            self.s.append(x)
        # If new number is less than minEle
        elif x < self.minEle:
            self.s.append(2 * x - self.minEle)
            self.minEle = x
        else:
            self.s.append(x)

    # Remove the top element from the Stack
    def pop(self):
        if not self.s:
            return

        top = self.s.pop()

        # Minimum will change, if the minimum element
        # of the stack is being removed.
        if top < self.minEle:
            self.minEle = 2 * self.minEle - top

    # Returns top element of Stack
    def peek(self):
        if not self.s:
            return -1

        top = self.s[-1]

        # If minEle > top means minEle stores value of top.
        return self.minEle if self.minEle > top else top

    # Finds minimum element of Stack
    def getMin(self):
        if not self.s:
            return -1

        # variable minEle stores the minimum element
        # in the stack.
        return self.minEle