'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


import collections
import time


# ! 20.163s
def sliding_window_max_1(nums, k):
    # Your code here
    container = []
    for i in range(0, len(nums)-(k-1)):
        container.append(max(nums[i:i+k]))
    return container


# ! 20.257s
# def sliding_window_max_2(nums, k):
#     # Your code here
#     d = Deque()
#     for i in range(0, len(nums)-(k-1)):
#         d.append(max(nums[i:i+k]))
#     return list(collections.deque((d)))


def sliding_window_max(nums, k):
    c = []
    i = 0
    # c.append(max)
    while k < len(nums)+1:
        c.append(max(nums[0:k]))
        nums.pop(0)
        # sliding_window_max(nums, k, c)
    return c


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
start = time.time()
print(sliding_window_max(arr, k))
end = time.time()
print(end-start)
'''
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
'''