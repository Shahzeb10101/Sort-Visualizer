import pygame
from math import floor

# FROM : https://www.youtube.com/watch?v=n_ijgqYmXS0

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size
        self.hovered = False
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- percentage

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])
        
    def render(self, window):
        pygame.draw.rect(window.screen, "darkgrey", self.container_rect)
        pygame.draw.rect(window.screen, "blue", self.button_rect)
    
    def move_slider(self, mouse_pos):
        self.button_rect.centerx = mouse_pos[0]
        
    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return floor((button_val/val_range)*(self.max-self.min)+self.min)
        
        

        