'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes_1(arr):
    # Your code here
    ind = []
    for i in range(0, len(arr)):
        if arr[i] == 0:
            ind.append(i)

    for i in reversed(range(len(ind))):
        arr.pop(ind[i])
        arr.append(0)
    return arr


def moving_zeroes(arr, i=1):
    if i == len(arr) + 1:
        return arr
    if arr[len(arr)-i] == 0:
        arr.pop(len(arr)-i)
        arr.append(0)

    return moving_zeroes(arr, i+1)


    # arr = [0, 0, 0, 0, 3, 2, 1]
arr = [0, 0, 0, 3, 0, 2, 1]
print(moving_zeroes(arr))


# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [0, 3, 1, 0, -2]

#     print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")