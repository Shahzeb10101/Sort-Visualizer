import pygame
from Classes import display
from helper import draw_sort_state

pygame.init()


def main():
    window = display(1200, 800)

    while window.running:
        window.clock.tick(window.FPS)
        # sorting Check (Techwithtim inspired)
        if window.sorting:
            try:
                next(window.generator)
            except StopIteration:
                window.sorting = False
                draw_sort_state(window, done=True, animate=True, clock=window.clock)
                window.done = True
        else:
            draw_sort_state(window, done=window.done)

        # Event Loop
        window.event_loop()

        pygame.display.update()


if __name__ == "__main__":
    main()
