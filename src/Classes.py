import pygame
import numpy as np
from random import shuffle, randint
from math import ceil

class display():
    
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