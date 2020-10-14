'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


# import collections
# import time


# # ! 20.163s
# def sliding_window_max_1(nums, k):
#     # Your code here
#     container = []
#     for i in range(0, len(nums)-(k-1)):
#         container.append(max(nums[i:i+k]))
#     return container


# # ! 20.257s
# # def sliding_window_max_2(nums, k):
# #     # Your code here
# #     d = Deque()
# #     for i in range(0, len(nums)-(k-1)):
# #         d.append(max(nums[i:i+k]))
# #     return list(collections.deque((d)))


# def sliding_window_max(nums, k):
#     c = []
#     i = 0
#     # c.append(max)
#     while k < len(nums)+1:
#         c.append(max(nums[0:k]))
#         nums.pop(0)
#         # sliding_window_max(nums, k, c)
#     return c


# arr = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# start = time.time()
# print(sliding_window_max(arr, k))
# end = time.time()
# print(end-start)

# Tom's Code 
from collections import deque

def sliding_window_max(nums, k):
    # max_vals = [0 for _ in range(len(nums) - k + 1)]
    
    # for i in range(len(max_vals)):
    #     current_elem = nums[i]
    #     for j in range(1, k):
    #         if nums[ i + j ] > current_elem:
    #             current_elem = nums[i+j]
    #     max_vals[i] = current_elem
    # return max_vals

    max_vals = []
    q = deque()
    # remove all elems from a queue
    for i, n in enumerate(nums):
        while len(q) > 0 and n > q[-1]:
            q.pop()
        q.append(n)
        # calc the window range
        window_range = i - k + 1
        # as long as out windows range == k, then we will add elements to the queue
        if window_range >= 0:
            # add the max elem (in this case 1st in the queue) to the max_vals
            max_vals.append(q[0])
            # check num on the left needs to be evicted
            # if sotake it out of the start of the queue
            if nums[window_range] == q[0]:
                q.popleft()
    return max_vals

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")


