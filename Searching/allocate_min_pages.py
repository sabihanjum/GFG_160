"""You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding)."""

def check(arr, k, pageLimit):
    #starting from the first student
    cnt = 1
    pageSum = 0
    for pages in arr:
        #if adding the current book exceed the page limit,
        #Assign the book to the next student
        if pageSum + pages > pageLimit:
            cnt += 1
            pageSum = pages
        else:
            pageSum += pages
    #if book can assign to less then k student then
    #it can be assigned to exactly k student as well
    return cnt <= k

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #if number students are more than total books
        #then allocation is not possible
        if k > len(arr):
            return -1
            
        #Search space for binary search
        lo = max(arr)
        hi = sum(arr)
        res = -1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if check(arr, k, mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res