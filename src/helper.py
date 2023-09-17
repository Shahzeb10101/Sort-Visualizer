import pygame
from math import ceil


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def bubble_sort(window, lst, clock):
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

    draw_sort_state(window)
    draw_sort_state(window, done=True, animate=True, clock=clock)


def merge_sort(window, lst, clock, relationstart, relationend, sortedlst):
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

    merge_sort(window, left_lst, clock, relstart, relend, sortedlst)

    relstart = relationstart + mid
    relend = relationend

    merge_sort(window, right_lst, clock, relstart, relend, sortedlst)

    return merge(left_lst, right_lst, lst, window, clock, relationstart, relationend)


def merge(left_lst, right_lst, final_lst, window, clock, relationstart, relationend):
    left_cursor = right_cursor = i = 0
    fps = window.FPS / 2
    while left_cursor < len(left_lst) and right_cursor < len(right_lst):
        window.event_loop()
        draw_sort_state(
            window,
            green=[left_cursor + relationstart],
            red=[right_cursor + relationstart],
            blue=[i + relationstart],
            update=True,
            clock=clock,
            fps=fps,
        )
        if left_lst[left_cursor] < right_lst[right_cursor]:
            window.lst[i + relationstart] = final_lst[i] = left_lst[left_cursor]
            i += 1
            left_cursor += 1
            draw_sort_state(
                window,
                green=[left_cursor + relationstart],
                red=[right_cursor + relationstart],
                blue=[i + relationstart],
                update=True,
                clock=clock,
                fps=fps,
            )
        else:
            window.lst[i + relationstart] = final_lst[i] = right_lst[right_cursor]
            i += 1
            right_cursor += 1
            draw_sort_state(
                window,
                green=[left_cursor + relationstart],
                red=[right_cursor + relationstart],
                blue=[i + relationstart],
                update=True,
                clock=clock,
                fps=fps,
            )

    while left_cursor < len(left_lst):
        window.lst[i + relationstart] = final_lst[i] = left_lst[left_cursor]
        i += 1
        left_cursor += 1
        draw_sort_state(
            window,
            green=[left_cursor + relationstart],
            red=[right_cursor + relationstart],
            blue=[i + relationstart],
            update=True,
            clock=clock,
            fps=fps,
        )

    while right_cursor < len(right_lst):
        window.lst[i + relationstart] = final_lst[i] = right_lst[right_cursor]
        i += 1
        right_cursor += 1
        draw_sort_state(
            window,
            green=[left_cursor + relationstart],
            red=[right_cursor + relationstart],
            blue=[i + relationstart],
            update=True,
            clock=clock,
            fps=fps,
        )

    return final_lst


def selection_sort(window, lst, clock):
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

    draw_sort_state(window)
    draw_sort_state(window, done=True, animate=True, clock=clock)


def draw_sort_state(
    window,
    green=[],
    red=[],
    blue=[],
    done=False,
    animate=False,
    clock=None,
    update=False,
    fps=0,
):
    if not done:
        window.screen.fill("black")
    x_pos = window.startx
    lst = window.lst
    for i in range(len(lst)):
        block_surf = pygame.Surface((window.block_width, lst[i] * 10))
        block_rect = block_surf.get_rect(bottomleft=(x_pos, 790))
        block_surf.fill("White")
        if green:
            if i in green:
                block_surf.fill("green")
        if red:
            if i in red:
                block_surf.fill("red")
        if blue:
            if i in blue:
                block_surf.fill("#08d2f7")
        if done:
            block_surf.fill("green")
            if animate:
                pygame.display.update(), clock.tick(40)

        x_pos += ceil(window.block_width / 10) + window.block_width
        window.screen.blit(block_surf, block_rect)
    if update:
        clock.tick(fps)
        pygame.display.update()
