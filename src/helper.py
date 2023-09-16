import pygame
from math import ceil

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    

def bubble_sort(window, lst, clock):
    length = len(lst)
    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            draw_sort_state(window, green=[j, j+1])
            if lst[j] > lst[j + 1]:
                swapped = True
                swap(lst, j, j + 1)
                draw_sort_state(window, green=[j], red=[j+1])
                yield True
        if not swapped:
            break
    
    draw_sort_state(window)
    draw_sort_state(window, done=True, animate=True, clock=clock)
    
    
def draw_sort_state(window, green=[], red=[], done=False, animate=False, clock=None):
    if not done: window.screen.fill("PURPLE")
    x_pos = window.startx
    lst = window.lst
    
    for i in range(len(lst)):
        block_surf = pygame.Surface((window.block_width, lst[i] * 10))
        block_rect = block_surf.get_rect(bottomleft = (x_pos, 790))
        block_surf.fill("White")
        if green:
            if i in green: block_surf.fill("green")
        if red:
            if i in red: block_surf.fill("red")
        if done:
            block_surf.fill("Black")
            if animate: pygame.display.update(), clock.tick(40)
        
        x_pos += ceil(window.block_width / 10) + window.block_width
        window.screen.blit(block_surf, block_rect)