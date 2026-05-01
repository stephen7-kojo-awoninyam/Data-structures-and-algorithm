def partition(unsorted_list, first_index, last_index):
            pivot = unsorted_list[first_index]
            greater_than_pivot_index = first_index + 1
            less_than_pivot_index = last_index
             
            while True:
                while unsorted_list[greater_than_pivot_index] < pivot and greater_than_pivot_index < less_than_pivot_index:
                    greater_than_pivot_index += 1
                while unsorted_list[less_than_pivot_index] > pivot and less_than_pivot_index >= greater_than_pivot_index:
                    less_than_pivot_index -= 1
                if greater_than_pivot_index < less_than_pivot_index:
                    temp = unsorted_list[less_than_pivot_index]
                    unsorted_list[less_than_pivot_index] = unsorted_list[greater_than_pivot_index]
                    unsorted_list[greater_than_pivot_index] = temp
                else:
                    break
            ramp = unsorted_list[less_than_pivot_index]
            unsorted_list[less_than_pivot_index] = unsorted_list[first_index]
            unsorted_list[first_index] = ramp
            return less_than_pivot_index



def quick_sort(unsorted_list,first,last):
    if last - first <= 0:
        return
    
    point = partition(unsorted_list,first,last)
    
    quick_sort(unsorted_list,first, point-1)
    
    quick_sort(unsorted_list,point+1,last)
    
unsorted_list = [43,3,20,89,4,77]
    
print(quick_sort(unsorted_list,0,5))   
    
                    
                        
                    








