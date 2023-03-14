'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):
    max_value = max(A)
    if max_value < 1:
        return 1
    # create a set containing all positive integers <= max_val
    nums_set = set(range(1, max_value+1))
    # remove positive integers from set if they appear in A
    for num in A:
        if num > 0 and num in nums_set:
            nums_set.remove(num)
    # return smallest positive integer in set or next integer if set is empty
    if not nums_set:
        return max_value + 1
    else:
        return min(nums_set)