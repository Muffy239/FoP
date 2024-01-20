def same(list1, list2):
    if len(list1) != len(list2):
        return False

    #* Count the frequency of each element in list1 and its square in list2
    list1_counter = {}
    list2_counter = {}

    for element in list1:
        list1_counter[element] = list1_counter.get(element, 0) + 1

    for element in list2:
        list2_counter[element] = list2_counter.get(element, 0) + 1
        
    print(list1_counter)
    print(list2_counter)

    #* Compare the frequency of each element in list1 with its square in list2
    for element in list1_counter:
        if list1_counter[element] != list2_counter.get(element ** 2, 0):
            return False

    return True

if __name__ == "__main__":
    print(same([1, 2, 3], [4, 1, 9])) # Should return True
    print(same([1, 2, 3], [1, 9])) # Should return False
    print(same([1, 2, 1], [4, 4, 1])) # Should return False
