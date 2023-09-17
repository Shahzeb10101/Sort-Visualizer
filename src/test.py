from helper import selection_sort, swap

x = [923, 2, 32, 4, 1, 9 , 8 , 23, 3, 1, 4, 67, 23, 6, 73, 53]

def insertion_sort(lst):
    for i in range(1,len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            swap(lst, j, j-1)
            j -= 1
            
print(x)
insertion_sort(x)
print(x)