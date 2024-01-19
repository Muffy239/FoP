def binarySearch(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        guess = sorted_list[mid]  # * our initial guess / pointer
        
        if guess == target:       #* Checks if we've found the target number
            return mid
        
        if guess > target:        #* If our guess it too high we guess lower
            high = mid - 1
        else:                     #* If our guess it too lower we guess higher
            low = mid + 1
            
    return -1                     #* the target is not in the list and we return -1


if __name__ == "__main__":
    print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) # 2
    print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
    print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1