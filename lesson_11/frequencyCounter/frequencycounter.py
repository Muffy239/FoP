def same(list1, list2):
    if len(list1) != len(list2):
        return f"\nAnswer:{False}\n"

    #* Count the frequency of each element in list1 and its square in list2
    
    list1_counter = {}
    list2_counter = {}

    for element in list1:
        list1_counter[element] = list1_counter.get(element, 0) + 1

    for element in list2:
        list2_counter[element] = list2_counter.get(element, 0) + 1
        
    print(f"Dictionary #1:\n{list1_counter}")
    print(f"Dictionary #2:\n{list2_counter}\n")

    #* Compare the frequency of each element in list1 with its square in list2
    #* We're just checking if the square of the Key in List1 exist as a key in list2. Not taking into account the keys position and if it's the same as List1.
    
    for key in list1_counter:
        if list1_counter[key] != list2_counter.get(key ** 2, 0):
            return f"Answer: {False}"

    return f"Answer: {True}"

if __name__ == "__main__":
    print(same([1, 2, 3], [4, 1, 9])) # Should return True
    print(same([1, 2, 3], [1, 9])) # Should return False
    print(same([1, 2, 1], [4, 4, 1])) # Should return False
