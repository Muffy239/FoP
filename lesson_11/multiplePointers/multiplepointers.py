
def sumZero(sorted_list):
    left = 0
    right = len(sorted_list) - 1

    while left < right:
        total = sorted_list[left] + sorted_list[right]
        if total == 0:
            return [sorted_list[left], sorted_list[right]]
        elif total > 0:
            right -= 1
        else:
            left += 1
    return -1


if __name__ == "__main__":
    print(sumZero([-3, -2, -1, 0, 1, 2, 3]))  # [-3, 3]
    print(sumZero([-10, -5, 0, 1, 3, 5, 87, 99]))  # [-5, 5]
    print(sumZero([-2, 0, 1, 3]))  # -1
    print(sumZero([1, 2, 3]))  # -1
