'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    res = arr[0] 
    # Do XOR of all elements and return 
    for i in range(1,len(arr)): 
        res = res ^ arr[i]

    return res
import random
# if __name__ == '__main__':
#     # Use the main function to test your implementation
arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

print(arr)
print(single_number(arr))
# print(f"The odd-number-out is {single_number(arr)}")
