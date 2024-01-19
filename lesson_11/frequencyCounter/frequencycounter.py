def same(list_1, list_2):
    if len(list_1) != len(list_2):
        return False

    counter_1 = {}
    counter_2 = {}

    # * counting each
    for value in list_1:
        counter_1[value] = counter_1.get(value, 1) + 1

    for value in list_2:
        counter_2[value] = counter_2.get(value, 1) + 1

    print(f"Dictionary 1: {counter_1}\nDictionary_2: {counter_2}\n")

    # ?  1st IF statement
    #!      counter_1 = {2: 1}
    #!      counter_2 = {4: 2}
    # ? 2nd IF Statement
    #!
    for key in counter_1:
        if (key**2) not in counter_2:  # * checks if the keys in counter 1 ^2 are equal to the key in
            return False
        if counter_1[key] != counter_2[key**2]:
            return False
    return True


if __name__ == "__main__":
    print(same([1, 2, 3], [4, 1, 9]))  # true
    print(same([1, 2, 3], [1, 9]))  # false
    print(same([1, 2, 1], [4, 4, 1]))  # false (must be same frequency)
