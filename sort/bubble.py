

def bubbleSort(unordered_list):
    
    list_size = len(unordered_list)
    
    i = 0
    
    while i < list_size:
    
        for j in range(list_size):
            try:
                if unordered_list[j] > unordered_list[j+1]:
                    
                    temp = unordered_list[j]
                    unordered_list[j] = unordered_list[j+1]
                    unordered_list[j+1] = temp
                    
                else:
                    continue  
            except IndexError:
                continue
        i += 1               
            
    return unordered_list




unordered_list = [2,4,3,1,8,5,7,9,6]
print(bubbleSort(unordered_list))          
        