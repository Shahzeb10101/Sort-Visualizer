from helper import draw_sort_state

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    
def bubble_sort(window, lst):
    length = len(lst)
    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            if lst[j] > lst[j + 1]:
                swapped = True
                swap(lst, j, j + 1)
                draw_sort_state(window, green=[j], red=[j + 1])
                yield True
        if not swapped:
            break

    draw_sort_state(window, done=True, animate=True)

def selection_sort(window, lst):
    length = len(lst)
    for i in range(length):
        minidx = i
        for j in range(i + 1, length):
            draw_sort_state(window, green=[j], red=[minidx])
            yield True
            if lst[j] < lst[minidx]:
                minidx = j
                draw_sort_state(window, green=[j], red=[minidx])
                yield True
        swap(lst, i, minidx)

    draw_sort_state(window, done=True, animate=True)
    
def insertion_sort(window, lst):
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            draw_sort_state(window, green=[i], red=[j])
            yield True
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
        yield True
    
    draw_sort_state(window, done=True, animate=True)

def quick_sort(window, lst, low, high):
    if low < high:
        pivot = partition(window, lst, low, high)
        
        quick_sort(window, lst, low, pivot - 1)
        quick_sort(window, lst, pivot + 1, high)
        
def partition(window, lst, low, high):
    pivot = lst[high]
    i = low 
    for j in range(low, high):
        draw_sort_state(window, green=[i], red=[j], blue=[high], update=True,)
        if lst[j] <= pivot:
            swap(lst, i ,j)
            i += 1

    draw_sort_state(window, green=[i], red=[j], blue=[high], update=True,)
    swap(lst, i ,high)

    return i

def merge_sort(window, lst, relationstart, relationend, sortedlst):
    length = len(lst)
    if length <= 1:
        return
    mid = length // 2
    left_lst = lst[:mid]
    right_lst = lst[mid:]

    relstart = relationstart
    if mid == 1:
        relend = relationstart
    else:
        relend = mid - 1 + relationstart

    merge_sort(window, left_lst, relstart, relend, sortedlst)

    relstart = relationstart + mid
    relend = relationend

    merge_sort(window, right_lst, relstart, relend, sortedlst)

    return merge(left_lst, right_lst, lst, window, relationstart, relationend)

def merge(left_lst, right_lst, final_lst, window, relationstart, relationend):
    left_cursor = right_cursor = i = 0
    relmid = (relationend + relationstart) // 2
    while left_cursor < len(left_lst) and right_cursor < len(right_lst):
        draw_sort_state(
            window,
            green=[left_cursor + relationstart],
            red=[right_cursor + relmid],
            blue=[i + relationstart],
            update=True,
        )
        if left_lst[left_cursor] < right_lst[right_cursor]:
            window.lst[i + relationstart] = final_lst[i] = left_lst[left_cursor]
            i += 1
            left_cursor += 1
            draw_sort_state(
                window,
                green=[left_cursor + relationstart],
                red=[right_cursor + relmid],
                blue=[i + relationstart],
                update=True,
            )
        else:
            window.lst[i + relationstart] = final_lst[i] = right_lst[right_cursor]
            i += 1
            right_cursor += 1
            draw_sort_state(
                window,
                green=[left_cursor + relationstart],
                red=[right_cursor + relmid],
                blue=[i + relationstart],
                update=True,
            )

    while left_cursor < len(left_lst):
        window.lst[i + relationstart] = final_lst[i] = left_lst[left_cursor]
        i += 1
        left_cursor += 1
        draw_sort_state(
            window,
            green=[left_cursor + relationstart],
            red=[right_cursor + relmid],
            blue=[i + relationstart],
            update=True,
        )

    while right_cursor < len(right_lst):
        window.lst[i + relationstart] = final_lst[i] = right_lst[right_cursor]
        i += 1
        right_cursor += 1
        draw_sort_state(
            window,
            green=[left_cursor + relationstart],
            red=[right_cursor + relmid],
            blue=[i + relationstart],
            update=True,
        )

    return final_lst