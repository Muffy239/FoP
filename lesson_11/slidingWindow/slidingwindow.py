def maxSubListSum(list, num):
    max_sum = 0
    curr_sum = 0

    if num > len(list):
        return None

    for i in range(num):
        max_sum += list[i]
    curr_sum = max_sum

    for j in range(num, len(list)):
        curr_sum = curr_sum - list[j - num] + list[j]
        max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 2))  # 10
    print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 4))  # 17
    print(maxSubListSum([4, 2, 1, 6], 1))  # 6
    print(maxSubListSum([4, 2, 1, 6, 2], 4))  # 13
    print(maxSubListSum([], 4))  # None
