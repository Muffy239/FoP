def binarySearch(list, target_num):
  low = 0
  high = len(list) - 1
  
  while low <= high:
    our_number = (low + high) // 2
    guess_in_list = list[our_number]
    
    if guess_in_list == target_num:
      return our_number
    
    if guess_in_list < target_num:
      low = our_number + 1
    
    elif guess_in_list > target_num:
      high = our_number - 1
      
  return -1

if __name__ == "__main__":
  print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) # 2
  print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
  print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1

