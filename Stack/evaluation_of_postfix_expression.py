"""You are given an array of strings arr that represents a valid arithmetic expression written in Reverse Polish Notation (Postfix Notation). Your task is to evaluate the expression and return an integer representing its value.

Key Details:

The valid operators are '+', '-', '*', and '/'.
Each operand is guaranteed to be a valid integer or another expression.
The division operation between two integers always rounds the result towards zero, discarding any fractional part.
No division by zero will occur in the input.
The input is a valid arithmetic expression in Reverse Polish Notation.
The result of the expression and all intermediate calculations will fit in a 32-bit signed integer."""

import math
class Solution:
    # Function that returns evaluated value of a given postfix expression
    def evaluatePostfix(arr: list[str]) -> int:
        stack = []

        for token in arr:
            # If token is a number, push it onto the stack
            if token.lstrip('-').isdigit():  
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if token == "+":
                    stack.append(val2 + val1)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val2 * val1)
                elif token == "/":
                    stack.append(math.trunc(val2 / val1))

        return stack.pop()