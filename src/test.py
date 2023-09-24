from helper import selection_sort, swap
from random import shuffle

x = [1, 2, 3, 4, 5]
shuffle(x)

def quick_sort(lst, low, high):
    if low < high:
        pivot = partition(lst, low, high)
        
        quick_sort(lst, low, pivot - 1)
        quick_sort(lst, pivot + 1, high)
        
def partition(lst, low, high):
    pivot = lst[high]
    
    i = low 
    for j in range(low, high):
        if lst[j] <= pivot:
            lst[i], lst[j] =  lst[j], lst[i]
            i += 1

    lst[i], lst[high] = lst[high] ,lst[i]

    return i
        
        
    

    
            
print(x)
quick_sort(x, 0, len(x) - 1)
print(x)