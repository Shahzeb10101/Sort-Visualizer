import pygame
from helper import draw_sort_state
from Classes import display

pygame.init()


def main():
    while window.running:
        window.clock.tick(window.FPS)
        # sorting Check (Techwithtim inspired)
        if window.sorting:
            try:
                next(window.generator)
            except StopIteration:
                draw_sort_state(window, done=True, animate=True)
                window.algo_done()
        else:
            draw_sort_state(window, done=window.done)
        
        # Event Loop
        window.event_loop()
        pygame.display.update()


if __name__ == "__main__":
    window = display(1200, 800)
    main()
