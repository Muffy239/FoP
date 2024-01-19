def binarySearch(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    #* Check if the 
    while low <= high:
        middle = (low + high) // 2  #* "//" is floor division returning the lowest whole number after the division is done 
        guess = sorted_list[middle] #* now that we have determined to middle of the book we throw our guess into the list
                                    #* and verify if we're correct. If NOT we find out if the guess was higher or lower than the  
        if guess == target:         #* target value.
            return middle
        
        if guess < target:        #* our guess is lower than the desired "target" number. so we try again.
            low = middle + 1
        
        elif guess > target:
            high = middle - 1
    
    return -1


if __name__ == "__main__":
    print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) # 2
    print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
    print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1