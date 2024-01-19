def bubbleSort(unordered_list):
    
    index_list = len(unordered_list) - 1
    sorted = False

    while not sorted:
        sorted = True #? stops it from looping again
        for i in range( 0, index_list):
            #? If current number greater than the next number we will swap their values
            if unordered_list[i] > unordered_list[i + 1]:
                sorted = False
                #? creates a tuple and swaps the values of the loop on the righthand side of the "=".
                (unordered_list[i], unordered_list[i+1]) = (unordered_list[i+1], unordered_list[i]) #? Flips the numbers
    return unordered_list


if __name__ == "__main__":
    print(bubbleSort([5, 3, 10, 6, 1])) # [1, 3, 5, 6, 10]
    print(bubbleSort([100, 98, 101, 10])) # [10, 98, 100, 101]
    print(bubbleSort([2, 1, 0, 5, 4])) # [0, 1, 2, 4, 5]
                
                
                