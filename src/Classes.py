import pygame
import numpy as np
from random import shuffle, randint
from math import ceil

from helper import draw_sort_state, bubble_sort, selection_sort, merge_sort, insertion_sort

class display(): 
    
    def __init__(self, width, height):
        self._WIDTH = width
        self._HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Visualizer")
        self.initialize_values()
        
        self.generate_list()
        self.buttons = pygame.sprite.Group()
        self.generate_buttons()
        
    def generate_buttons(self):
        self.button_x_pos = 30
        self.buttons.add(Button("I - Insertion Sort", self.button_x_pos, 50, self, function=self.start_insertion_sort))
        self.buttons.add(Button("B - Bubble Sort", self.button_x_pos, 50, self, function=self.start_bubble_sort))
        self.buttons.add(Button("M - Merge Sort", self.button_x_pos, 50, self, function=self.start_merge_sort))
        self.buttons.add(Button("S - Selection Sort", self.button_x_pos, 50, self, function=self.start_selection_sort))
        self.buttons.add(Button("L - RandList", self.button_x_pos, 50, self, function=self.generate_list))
        self.buttons.add(Button("J - SetList", self.button_x_pos, 50, self, function=self.generate_list, arg='default_list=True'))
    
    def initialize_values(self):
        self._MIN_VAL = 1
        self._MAX_VAL = 100
        self._min_list_size = 5
        self._max_list_size = 300
        self._SIDE_PADDING = 100
        self._TOP_PADDING = 200
        self.running = True
        self.sorting = False
        self.done = False
        self.generator = None
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.rainbow = False
        self.font = pygame.font.Font(size=28)
    
    # Default list is 0 to MAX
    def generate_list(self, default_list = False):
        if default_list:
            self.lst = list(range(self._MIN_VAL, self._MAX_VAL + 1))
            shuffle(self.lst)
        else:
            self.lst = list(np.random.randint(low = self._MIN_VAL,high = self._MAX_VAL,size=randint(self._min_list_size, self._max_list_size)))
        self.block_width = (self._WIDTH - self._SIDE_PADDING) / len(self.lst)
        self.block_width -= ceil(self.block_width / 10)
        self.block_height_scale = (self._HEIGHT - self._TOP_PADDING) / (max(self.lst) - min(self.lst))
        
        self.startx = (self._WIDTH - (ceil(self.block_width / 10) * len(self.lst) + self.block_width * len(self.lst))) // 2
        
    # event loop
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if not self.sorting:
                    if event.key == pygame.K_l:
                        self.generate_list()
                        self.done = False
                    if event.key == pygame.K_j:
                        self.generate_list(default_list=True)
                        self.done = False
                    if event.key == pygame.K_b:
                        self.start_bubble_sort()
                    if event.key == pygame.K_s:
                        self.start_selection_sort()
                    if event.key == pygame.K_m:
                        self.start_merge_sort()
                    if event.key == pygame.K_i:
                        self.start_insertion_sort()
                if event.key == pygame.K_n:
                    self.rainbow = not self.rainbow
            for button in self.buttons:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.sorting:
                        if button.rect.collidepoint(event.pos):
                            if button.arg:
                                button.function(button.arg)
                            else:
                                button.function()
        self.buttons.update()
        
                    
    def algo_start(self):
        self.sorting = True
        self.done = False
    
    def start_insertion_sort(self):
        self.generator = insertion_sort(self, self.lst, self.clock)
        self.algo_start()
        
    def start_merge_sort(self):
        self.sorting = True
        self.lst = merge_sort(self, self.lst, self.clock, 0, len(self.lst), sorted(self.lst))
        self.sorting = False
        self.done = True
        draw_sort_state(self)
        draw_sort_state(self, done=True, animate=True, clock=self.clock)
        
    def start_bubble_sort(self):
        self.generator = bubble_sort(self, self.lst, self.clock)
        self.algo_start()
        
    def start_selection_sort(self):
        self.generator = selection_sort(self, self.lst, self.clock)
        self.algo_start()

class Button(pygame.sprite.Sprite):
    def __init__(self, text, top_x, top_y, window, function=None, arg=''):
        super().__init__()
        self.image = window.font.render(text, True, "White")
        window.button_x_pos += window.font.size(text)[0] + 30
        self.rect = self.image.get_rect(topleft = (top_x, top_y))
        self.arg = arg
        self.function = function

        