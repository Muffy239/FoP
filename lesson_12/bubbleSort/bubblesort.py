def bubbleSort(unordered_list):
    list_length = len(unordered_list) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        
        for number in range(0, list_length):

            if unordered_list[number] > unordered_list[number + 1]:
                sorted = False
                (unordered_list[number], unordered_list[number + 1]) = (unordered_list[number + 1], unordered_list[number])
    return unordered_list



if __name__ == "__main__":
    print(bubbleSort([5, 3, 10, 6, 1])) # [1, 3, 5, 6, 10]
    print(bubbleSort([100, 98, 101, 10])) # [10, 98, 100, 101]
    print(bubbleSort([2, 1, 0, 5, 4])) # [0, 1, 2, 4, 5]
