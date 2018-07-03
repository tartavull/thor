import sys

from evdev import ecodes
import pygame

def get_square_positions(
    margin_left=20, margin_top=20, hand_separation=20,
    button_width=75, button_padding=2):

    #column_positions
    c1_min = margin_left
    c1_max = c1_min + button_width
    c2_min = c1_max + button_padding
    c2_max = c2_min + button_width
    c3_min = c2_max + hand_separation
    c3_max = c3_min + button_width
    c4_min = c3_max + button_padding
    c4_max = c4_min + button_width
    screen_width = c4_max + margin_left
    
    #row positions
    r1_min = margin_top
    r1_max = r1_min + button_width
    r2_min = r1_max + button_padding
    r2_max = r2_min + button_width
    r3_min = r2_max + button_padding
    r3_max = r3_min + button_width
    r4_min = r3_max + button_padding
    r4_max = r4_min + button_width
    r5_min = r4_max + button_padding  + margin_top
    r5_max = r5_min + button_width
    r6_min = r5_max + button_padding
    r6_max = r6_min + button_width
    screen_height = r6_max + margin_top

    button_pos = [
        (c2_min, r6_min, c2_max - c2_min, r6_max - r6_min),
        (c1_min, r6_min, c1_max - c1_min, r6_max - r6_min),
        (c2_min, r5_min, c2_max - c2_min, r5_max - r5_min),
        (c1_min, r5_min, c1_max - c1_min, r5_max - r5_min),
        (c2_min, r4_min, c2_max - c2_min, r4_max - r4_min),
        (c1_min, r4_min, c1_max - c1_min, r4_max - r4_min),
        (c2_min, r3_min, c2_max - c2_min, r3_max - r3_min),
        (c1_min, r3_min, c1_max - c1_min, r3_max - r3_min),
        (c2_min, r2_min, c2_max - c2_min, r2_max - r2_min),
        (c1_min, r2_min, c1_max - c1_min, r2_max - r2_min),
        (c2_min, r1_min, c2_max - c2_min, r1_max - r1_min),
        (c1_min, r1_min, c1_max - c1_min, r1_max - r1_min),
        (c3_min, r6_min, c3_max - c3_min, r6_max - r6_min),
        (c4_min, r6_min, c4_max - c4_min, r6_max - r6_min),
        (c3_min, r5_min, c3_max - c3_min, r5_max - r5_min),
        (c4_min, r5_min, c4_max - c4_min, r5_max - r5_min),
        (c3_min, r4_min, c3_max - c3_min, r4_max - r4_min),
        (c4_min, r4_min, c4_max - c4_min, r4_max - r4_min),
        (c3_min, r3_min, c3_max - c3_min, r3_max - r3_min),
        (c4_min, r3_min, c4_max - c4_min, r3_max - r3_min),
        (c3_min, r2_min, c3_max - c3_min, r2_max - r2_min),
        (c4_min, r2_min, c4_max - c4_min, r2_max - r2_min),
        (c3_min, r1_min, c3_max - c3_min, r1_max - r1_min),
        (c4_min, r1_min, c4_max - c4_min, r1_max - r1_min)] 

    return screen_width, screen_height, button_pos

def get_char(key):
    if type(key.symbol) is tuple:
        label, font = key.symbol
        font = pygame.font.Font(font,30)
    else:
        font = pygame.font.Font("ui-symbol.ttf",30)
        label = key.symbol
    return font.render(label, 1, (0,0,0))

def draw_square(pos, key_code, pressed=False):
    color =  (250,100,100) if pressed  else (100,100,250)
    pygame.draw.rect(screen, color, pos, 0)
    label = get_char(key_code)
    screen.blit(label, (pos[0]+20, pos[1]+20))

def update(keys, pressed):
    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

    # erase the screen
    white = (255,255,255)
    screen.fill(white)

    #draw_rectangles(screen)
    for button, key in enumerate(keys):
        draw_square(square_positions[button], key, button in pressed)

    pygame.display.update()


pygame.init()
width, height, square_positions = get_square_positions()
screen = pygame.display.set_mode((width , height))

if __name__ == '__main__':
    update([ecodes.KEY_QUESTION]*24)
