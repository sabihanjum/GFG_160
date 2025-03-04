"""A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. A square matrix mat[][] (n*n) is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing"""

def celebrity(mat):
    n = len(mat)

    i = 0
    j = n - 1
    while i < j:
        
        # j knows i, thus j can't be celebrity
        if mat[j][i] == 1:
            j -= 1
        
        # else i can't be celebrity
        else:
            i += 1

    # i points to our celebrity candidate
    c = i

    # Check if c is actually
    # a celebrity or not
    for i in range(n):
        if i == c:
            continue
        
        # If any person doesn't
        # know 'c' or 'c' doesn't
        # know any person, return -1
        if mat[c][i] or not mat[i][c]:
            return -1

    return c