def median_of_the_medians(element):
    sublists = [element[j:j+5] for j in range(0,len(element),5)]
    
    median = []
    
    for sublist in sublists:
        median.append(sorted(sublist)[len(sublist)//2])
        
    return sorted(median)[len(median)//2] 


def find_median_index(unsorted_list,first,last,median):
    if first == last:
        return first
    
    return first + unsorted_list.index(median)

def swap(unsorted_list,first,index):
    temp = unsorted_list[index]
    unsorted_list[index] = unsorted_list[first]
    unsorted_list[first] = temp
 
   

def partition(unsorted_list,first,last):
    if first == last:
        return first
    
    median = median_of_the_medians(unsorted_list[first:last])
    median_index = find_median_index(unsorted_list,first,last,median)
    
    swap(unsorted_list, first,median_index)
    
    
    pivot = unsorted_list[first]
    
    greater_than_pivot_index = first + 1
    
    less_than_pivot_index = last
    
    while True:
        while unsorted_list[greater_than_pivot_index] < pivot and greater_than_pivot_index < less_than_pivot_index:
            greater_than_pivot_index += 1
        while unsorted_list[less_than_pivot_index] > pivot and less_than_pivot_index > greater_than_pivot_index:
            less_than_pivot_index -= 1
            
        if  unsorted_list[greater_than_pivot_index] > unsorted_list[less_than_pivot_index]:
            temp = unsorted_list[greater_than_pivot_index]
            unsorted_list[greater_than_pivot_index] = unsorted_list[less_than_pivot_index]
            unsorted_list[less_than_pivot_index] = temp
        else:
            break
    
    
    ramp = unsorted_list[first]
    unsorted_list[first] = unsorted_list[less_than_pivot_index]
    unsorted_list[less_than_pivot_index] = ramp
    
    
    return less_than_pivot_index




def selection(unsorted_list, first, last,k):
    
    split = partition(unsorted_list,first,last)
    
    if k == split:
        return unsorted_list[split]
    
    if k < split:
        return selection(unsorted_list, first, split-1,k)
    else:
        return selection(unsorted_list,split+1,last,k) 
    
            
    


print(selection([7,6,5,4,3,2,1],0,6,3))

    
    











