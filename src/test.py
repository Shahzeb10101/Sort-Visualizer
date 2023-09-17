from helper import selection_sort

x = [923, 2, 32, 4, 1, 9 , 8 , 23, 3, 1, 4, 67, 23, 6, 73, 53]

def merge_sort(lst):
    length = len(lst)
    if length <= 1:
        return
    mid = length // 2
    left_lst = lst[:mid]
    right_lst = lst[mid:]
    
    merge_sort(left_lst)
    merge_sort(right_lst)
    return merge(left_lst, right_lst, lst)
    
def merge(left_lst, right_lst, final_lst):
    left_cursor = right_cursor = i = 0
    while left_cursor < len(left_lst) and right_cursor < len(right_lst):
        if left_lst[left_cursor] < right_lst[right_cursor]:
            final_lst[i] = left_lst[left_cursor]
            i += 1
            left_cursor += 1
        else:
            final_lst[i] = right_lst[right_cursor]
            i += 1
            right_cursor += 1
            
    while left_cursor < len(left_lst):
        final_lst[i] = left_lst[left_cursor]
        i += 1
        left_cursor += 1
        
    while right_cursor < len(right_lst):
        final_lst[i] = right_lst[right_cursor]
        i += 1
        right_cursor += 1
        
    return final_lst

print(x)       
merge_sort(x)
print(x)