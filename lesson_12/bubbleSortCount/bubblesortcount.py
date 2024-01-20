def bubbleSortCount(list):
        list_length = len(list) -1
        compare_count = 0
        exchange_count = 0
        
        for i in range(list_length,-1,-1):
                for j in range(i):
                        compare_count += 1
                        if list[j] > list[j + 1]:
                                exchange_count += 1
                                (list[j], list[j + 1]) = (list[j+1], list[j])
                                
        return  (compare_count, exchange_count), list



if __name__ == "__main__":

        print(bubbleSortCount([1, 2, 3, 5, 4, 6, 7])) # (21, 1)
        print(bubbleSortCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # (45, 45)
        print(bubbleSortCount([2, 1, 0, 5, 4])) # (10, 4)