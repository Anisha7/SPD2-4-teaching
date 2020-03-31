# Array Problems
# Using your idea sketches, pseudocode, or whiteboard code 
# from the brainstorming session, type it in your code editor, 
# run some test cases, and debug your code so it works correctly. 
# Implement at least 2 different solutions for each of the 3 
# problems above (6+ solutions total).

## Problem 1
# Given an array a of n numbers and a target value t, find two 
# numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  ⇒  [3, 7] or [6, 4] or [8, 2]

# Simplifications:
# 1. Assume there are no duplicates.
# 2. Assume the array is sorted.
# 3. Assume all positives

# Psuedocode V1:
    # sort the array
    # loop over the array
        # loop over the curr index to end of array
            # check if the two numbers add up to t
            # if yes, return
    # return none because no solution was found

# Solution V1:
def twoSum1(a, t):
    # Time: O(n**2) because of the nested for loop, O(n(n-1) + nlogn) simplified. 
    # Space: O(1) because we are using an inplace sorting algorithm
    a.sort()
    for i in range(len(a)):
        for j in range(i, len(a)):
            if (a[i] + a[j] == t):
                return [a[i], a[j]]
    return None

# Psuedocode V2:
    # sort the array
    # track first and last item of array as i and j
        # if first + last < t, then increment first
        # if its > t, then decrement last
        # if equal: return
    # return none

# Solution V2:
def twoSum2(a, t):
    # Time:  O(N)
    # Space: O(1) because we are using an inplace sorting algorithm
    a.sort()
    i = 0
    j = len(a) - 1
    while i < j and j < len(a):
        if (a[i] + a[j] == t):
            return [a[i], a[j]]
        elif (a[i] + a[j] < t):
            i += 1
        else:
            j -= 1
    return None

# Test
def testTwoSum(fn):
    # Simple test
    res = set(fn([5, 3, 6, 8, 2, 4, 7], 10))
    assert(res == {3, 7} or res == {6, 4} or res == {8, 2})
    # With duplicates [1,2,2,3,4,5,6,7,8]
    res = set(fn([5, 3, 6, 8, 2, 4, 7, 2, 1], 4))
    assert(res == {2, 2} or res =={3, 1})
    # With negatives
    res = set(fn([5, 3, 6, 8, 2, 4, 7, -1], 7))
    assert(res == {5, 2} or res == {8, -1} or res == {4, 3})

## Problem 2
# Given an array a of n numbers and a count k find the k 
# largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

# Simplifications:
# 1.
# 2.
# 3.

# Psuedocode V1:

# Solution V1:

# Psuedocode V2:

# Solution V2:

# Test


## Problem 3
# Given two arrays a and b of numbers and a target value t, 
# find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  
# t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

# Simplifications:
# 1.
# 2.
# 3.

# Psuedocode V1:

# Solution V1:

# Psuedocode V2:

# Solution V2:

# Test



#### main test
if __name__ == '__main__':
    print("Testing TwoSum Version 1...")
    testTwoSum(twoSum1)
    print("Passed.")
    print("Testing TwoSum Version 2...")
    testTwoSum(twoSum2)
    print("Passed.")