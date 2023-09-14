import pygame
import numpy as np
from random import randint

def randomize():
    global x
    x = list(np.random.randint(low = 0,high=75,size=randint(5, 100)))
    global width
    width = 700 / len(x)
    width = width - width / 10
    print(len(x), width)

def swap(arr, j1, j2):
    temp = arr[j1]
    arr[j1] = arr[j2]
    arr[j2] = temp

def bubble(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            update(nums, [j, j + 1])
            if nums[j] > nums[j + 1]:
                swapped = True
                swap(nums, j, j + 1)
        if not swapped:
            break        
                
                
def update(arr, green):
    print(green)
    screen.fill("purple")
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    y = 50
    for i in range(len(arr)):
        block_surf = pygame.Surface((width,arr[i] * 10))
        block_rect = block_surf.get_rect(midbottom = (y, 790))
        y += int(width / 10 + width)
        if not i in green:
            block_surf.fill("White")
        else:
            block_surf.fill("Green")
        screen.blit(block_surf, block_rect)
    pygame.display.update()
    clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:     
                    bubble(x)
                if event.key == pygame.K_l:
                    randomize()
                    print(x)
        pygame.display.update()
        clock.tick(10)

randomize()
main()