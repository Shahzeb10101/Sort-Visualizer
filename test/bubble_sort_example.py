import pygame
import numpy as np
from random import randint, shuffle
from math import ceil

complete = False

def randomize(num):
    global x
    if num == 0:
      x = list(np.random.randint(low = 5,high=70,size=randint(5, 100)))
    else:
      x = list(range(1,71))
      shuffle(x)
    global width
    width = 700 / len(x)
    width = width - ceil(width / 10)
    print(len(x), width)
    complete = False

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
            complete = True
            break
    print(nums)
               
               
def update(arr, green):
    screen.fill("purple")
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    y = 50
    for i in range(len(arr)):
        block_surf = pygame.Surface((width,arr[i] * 10))
        block_rect = block_surf.get_rect(bottomleft = (y, 720))
        y += ceil(width / 10) + width
        if green:
          if i in green:
              block_surf.fill("Green")
        if complete:
          block_surf.fill("Red")
        else:
          block_surf.fill("White")
           
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
                    randomize(0)
                    print(x)
                if event.key == pygame.K_j:
                    randomize(1)
                    print(x)
        update(x, [])
        pygame.display.update()
        clock.tick(1000)

randomize(0)
main()