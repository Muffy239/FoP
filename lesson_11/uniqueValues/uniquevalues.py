def countUniqueValues(s_list):
    unique_list = list(set(s_list))
    return len(unique_list)


if __name__ == "__main__":
    print(countUniqueValues([1, 1, 1, 1, 1, 2]))  # 2
    print(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]))  # 7
    print(countUniqueValues([-2, -1, -1, 0, 1]))  # 4
    print(countUniqueValues([]))  # 0
