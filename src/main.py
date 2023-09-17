import pygame
from Classes import display
from helper import draw_sort_state, bubble_sort, selection_sort, merge_sort

pygame.init()


def main():
    clock = pygame.time.Clock()
    running = True
    window = display(1200, 800)
    sorting = False
    done = False
    generator = None
    FPS = 60
    
    while running:
        clock.tick(FPS)
        #sorting Check (Techwithtim inspired)
        if sorting:
            try:
                next(generator)
            except StopIteration:
                sorting = False
                draw_sort_state(window, done=True, animate=True, clock=clock)
                done = True
        else:
            draw_sort_state(window, done=done)
        
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if not sorting:
                    if event.key == pygame.K_l:
                        window.generate_list()
                        done = False
                    if event.key == pygame.K_j:
                        window.generate_list(default_list=True)
                        done = False
                    if event.key == pygame.K_k:
                        generator = bubble_sort(window, window.lst, clock)
                        sorting = True
                        done = False
                    if event.key == pygame.K_h:
                        generator = selection_sort(window, window.lst, clock)
                        sorting = True
                        done = False
                    if event.key == pygame.K_m:
                        sorting = True
                        window.lst = merge_sort(window, window.lst, clock, 0, len(window.lst), sorted(window.lst))
                        done = True
                        draw_sort_state(window)
                        draw_sort_state(window, done=True, animate=True, clock=clock)
                        sorting = False
                    
        pygame.display.update()
          
if __name__ == "__main__":
    main()