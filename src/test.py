from helper import selection_sort, swap

x = [923, 2, 32, 4, 1, 9 , 8 , 23, 3, 1, 4, 67, 23, 6, 73, 53]

def insertion_sort(lst):
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
            
print(x)
insertion_sort(x)
print(x)