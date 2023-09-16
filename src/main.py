import pygame
import numpy as np
from random import shuffle, randint
from math import ceil
pygame.init()

class display():
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    
    def __init__(self, width, height):
        self._WIDTH = width
        self._HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Visualizer")
        
        self._MIN_VAL = 1
        self._MAX_VAL = 70
        self._min_list_size = 5
        self._max_list_size = 50
        self._PADDING = 100
        
        self.generate_list()
    
    # Default list is 0 to MAX
    def generate_list(self, default_list = False):
        if default_list:
            self.lst = list(range(self._MIN_VAL, self._MAX_VAL + 1))
            shuffle(self.lst)
        else:
            self.lst = list(np.random.randint(low = self._MIN_VAL,high = self._MAX_VAL,size=randint(self._min_list_size, self._max_list_size)))
        self.block_width = (self._WIDTH - self._PADDING) / len(self.lst)
        self.block_width -= ceil(self.block_width / 10)
        
        self.startx = (self._WIDTH - (ceil(self.block_width / 10) * len(self.lst) + self.block_width * len(self.lst))) // 2
            
    
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    

def bubble_sort(window, lst, clock):
    length = len(lst)
    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            draw_sort_state(window, clock, green=[j, j+1])
            if lst[j] > lst[j + 1]:
                swapped = True
                swap(lst, j, j + 1)
                draw_sort_state(window, clock, green=[j], red=[j+1])
                yield True
                
                

def draw_sort_state(window, clock, green=[], red=[]):
    window.screen.fill("PURPLE")
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
        
        x_pos += ceil(window.block_width / 10) + window.block_width
        window.screen.blit(block_surf, block_rect)
    pygame.display.update()
        

def main():
    clock = pygame.time.Clock()
    running = True
    window = display(800, 800)
    sorting = False
    
    while running:
        clock.tick(60)
        if sorting:
            try:
                next(gen)
            except StopIteration:
                sorting = False
        else:
            draw_sort_state(window, clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    window.generate_list()
                if event.key == pygame.K_j:
                    window.generate_list(default_list=True)
                if event.key == pygame.K_k and not sorting:
                    gen = bubble_sort(window, window.lst, clock)
                    sorting = True
                  
        
        pygame.display.update()
          
if __name__ == "__main__":
    main()