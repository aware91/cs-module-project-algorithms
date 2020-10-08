'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, arr=[]):
    dict = [1, 1, 2, 4]
    i = 4
    if n < 4:
        return dict[n]
    else:
        while i <= n:
            dict.append(sum(dict[i-3:i]))
            i += 1

    return dict[len(dict)-1]


print(eating_cookies(500))

# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(
#         f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")