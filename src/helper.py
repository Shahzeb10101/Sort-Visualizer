import pygame
from math import ceil,sin

def draw_sort_state(
    window,
    green=[],
    red=[],
    blue=[],
    done=False,
    animate=False,
    update=False,
    ):
    if not done:
        window.screen.fill("black")
    x_pos = window.startx
    lst = window.lst
    if animate:  draw_sort_state(window)
    for i in range(len(lst)):
        block_surf = pygame.Surface((window.block_width, lst[i] * window.block_height_scale))
        block_rect = block_surf.get_rect(bottomleft=(x_pos, 800))
        block_surf.fill("white")
        if green:
            if i in green:
                block_surf.fill("green")
        if red:
            if i in red:
                block_surf.fill("red")
        if blue:
            if i in blue:
                block_surf.fill("#08d2f7")
        if window.rainbow:
            block_surf.fill(num_to_rgb(lst[i], max(lst)))
        if done and not window.rainbow:
            block_surf.fill("green")
            if animate:
                pygame.display.update()

        x_pos += ceil(window.block_width / 10) + window.block_width
        window.buttons.draw(window.screen)
        window.screen.blit(block_surf, block_rect)
        window.lst_slider.render(window)
        window.fps_slider.render(window)
    if update:
        window.clock.tick(window.FPS)
        pygame.display.update()
        window.event_loop()
        
def num_to_rgb(val, max_val=3):
    i = (val * 255 / max_val)
    r = round(sin(0.024 * i + 0) * 127 + 128)
    g = round(sin(0.024 * i + 2) * 127 + 128)
    b = round(sin(0.024 * i + 4) * 127 + 128)
    return (r,g,b)
