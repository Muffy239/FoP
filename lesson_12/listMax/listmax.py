def list_max(list, max_num = None):
    if not list:
        return max_num
    
    current_element = list[0]
    
    if max_num is None or current_element > max_num:
        max_num = current_element
    return list_max(list[1:],max_num) #? [ 1: ] deletes the 1st element
    
num = list_max([5,4,10])
print(num)