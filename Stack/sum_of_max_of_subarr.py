"""Given an array arr[], the task is to find the sum of the maximum elements of every possible non-empty sub-arrays of the given array arr[].

Note: The answer will always fit into 32 bit integer."""

def sumOfMax(arr):
    n = len(arr)
    res = 0
    stk = []
    left = [0] * n
    right = [0] * n

    # Finding the left boundary for each element
    for i in range(n):

        # Pop elements smaller than arr[i] from stack
        while stk and arr[stk[-1]] < arr[i]:
            stk.pop()

        # Calculate left boundary count
        left[i] = (i + 1) if not stk else (i - stk[-1])

        # Push current index into stack
        stk.append(i)

    # Clear the stack for right boundary computation
    stk.clear()

    # Finding the right boundary for each element
    for i in range(n - 1, -1, -1):

        # Pop elements smaller or equal to arr[i] from stack
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        # Calculate right boundary count
        right[i] = (n - i) if not stk else (stk[-1] - i)

        # Push current index into stack
        stk.append(i)

    # Compute sum of max elements of all subarrays
    for i in range(n):

        # Contribution of arr[i] as max in subarrays
        res += arr[i] * left[i] * right[i]

    return res