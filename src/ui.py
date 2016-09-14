import pygame
import sys

screen_width , screen_height = 350 , 500
margin_left = 10
button_width = 75
button_padding = 2
hand_separation = 20

c1_min = margin_left
c1_max = c1_min + button_width
c2_min = c1_max + button_padding
c2_max = c2_min + button_width
c3_min = c2_max + hand_separation
c3_max = c3_min + button_width
c4_min = c3_max + button_padding
c4_max = c4_min + button_width

margin_top = screen_height / 30
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

kmap = {
  'l1': (c2_min, r6_min, c2_max - c2_min, r6_max - r6_min),
  'l2': (c1_min, r6_min, c1_max - c1_min, r6_max - r6_min),
  'l3': (c2_min, r5_min, c2_max - c2_min, r5_max - r5_min),
  'l4': (c1_min, r5_min, c1_max - c1_min, r5_max - r5_min),
  'l5': (c2_min, r4_min, c2_max - c2_min, r4_max - r4_min),
  'l6': (c1_min, r4_min, c1_max - c1_min, r4_max - r4_min),
  'l7': (c2_min, r3_min, c2_max - c2_min, r3_max - r3_min),
  'l8': (c1_min, r3_min, c1_max - c1_min, r3_max - r3_min),
  'l9': (c2_min, r2_min, c2_max - c2_min, r2_max - r2_min),
  'l10':(c1_min, r2_min, c1_max - c1_min, r2_max - r2_min),
  'l11':(c2_min, r1_min, c2_max - c2_min, r1_max - r1_min),
  'l12':(c1_min, r1_min, c1_max - c1_min, r1_max - r1_min),
  'r1': (c3_min, r6_min, c3_max - c3_min, r6_max - r6_min),
  'r2': (c4_min, r6_min, c4_max - c4_min, r6_max - r6_min),
  'r3': (c3_min, r5_min, c3_max - c3_min, r5_max - r5_min),
  'r4': (c4_min, r5_min, c4_max - c4_min, r5_max - r5_min),
  'r5': (c3_min, r4_min, c3_max - c3_min, r4_max - r4_min),
  'r6': (c4_min, r4_min, c4_max - c4_min, r4_max - r4_min),
  'r7': (c3_min, r3_min, c3_max - c3_min, r3_max - r3_min),
  'r8': (c4_min, r3_min, c4_max - c4_min, r3_max - r3_min),
  'r9': (c3_min, r2_min, c3_max - c3_min, r2_max - r2_min),
  'r10':(c4_min, r2_min, c4_max - c4_min, r2_max - r2_min),
  'r11':(c3_min, r1_min, c3_max - c3_min, r1_max - r1_min),
  'r12':(c4_min, r1_min, c4_max - c4_min, r1_max - r1_min) 
}

status = {
  'l1': {'label':'key', 'down':False},
  'l2': {'label':'key', 'down':False},
  'l3': {'label':'key', 'down':False},
  'l4': {'label':'key', 'down':False},
  'l5': {'label':'key', 'down':False},
  'l6': {'label':'key', 'down':False},
  'l7': {'label':'key', 'down':False},
  'l8': {'label':'key', 'down':False},
  'l9': {'label':'key', 'down':False},
  'l10':{'label':'key', 'down':False},
  'l11':{'label':'key', 'down':False},
  'l12':{'label':'key', 'down':False},
  'r1': {'label':'key', 'down':False},
  'r2': {'label':'key', 'down':False},
  'r3': {'label':'key', 'down':False},
  'r4': {'label':'key', 'down':False},
  'r5': {'label':'key', 'down':False},
  'r6': {'label':'key', 'down':False},
  'r7': {'label':'key', 'down':False},
  'r8': {'label':'key', 'down':False},
  'r9': {'label':'key', 'down':False},
  'r10':{'label':'key', 'down':False},
  'r11':{'label':'key', 'down':False},
  'r12':{'label':'key', 'down':False} 
}

def render_unicode(label):
  if len(label) == 2:
    label, font = label
    font = pygame.font.Font(font,30)
  else:
    label =  label[0]
    font = pygame.font.Font("ui-symbol.ttf",30)

  return font.render(label, 1, (0,0,0))
pygame.init()

screen = pygame.display.set_mode((screen_width , screen_height))
clock =  pygame.time.Clock()

def draw_rectangles(screen):

  for k,v in kmap.iteritems():
    if status[k]['down']:
      color =  (250,100,100)
    else:
      color = (100,100,250)
    
    pygame.draw.rect(screen, color, v, 0)
    if type(status[k]['label']) is list:
      label = render_unicode(status[k]['label'][0])
      screen.blit(label, (v[0]+10, v[1]+5))
      label = render_unicode(status[k]['label'][1])
      screen.blit(label, (v[0]+10, v[1]+30))
    else:
      label = render_unicode(status[k]['label'])
      screen.blit(label, (v[0]+10, v[1]+5))


#


def update():

  # check for quit events
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
           pygame.quit(); sys.exit();

  # erase the screen
  white = (255,255,255)
  screen.fill(white)


  #draw keys
  draw_rectangles(screen)

  # update the screen
  msElapsed = clock.tick(30)
  pygame.display.update()


update()