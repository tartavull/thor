#how to use x-input to disable adafruit and know where to read from them
#http://askubuntu.com/questions/160945/is-there-a-way-to-disable-a-laptops-internal-keyboard
#xinput float {id}

# #then make all the even files readable but the user running this script
# # sudo chmod a+r /dev/input/event*


from evdev import InputDevice, categorize, ecodes ,UInput
print ecodes.__file__
from select import select
import ui

# A mapping of file descriptors (integers) to InputDevice instances.
devices = map(InputDevice, ('/dev/input/event14','/dev/input/event15')) 
# devices = map(InputDevice, ('/dev/input/event3',)) 

devices = {dev.fd: dev for dev in devices}

for dev in devices.values(): 
  print(dev)
  dev.grab()

from collections import defaultdict
dmap = { 'a403':'r', 'a496':'l', 'oard':'r'}
kmap_hard = { 'r': {28:1,
               2:2,
               106:3,
               57:4,
               103:5,
               3:6,
               108:7,
               17:8,
               105:9,
               30:10,
               31:11,
               32:12},
          'l': {108:1,
               17:2,
               103:3,
               57:4,
               105:5,
               28:6,
               106:7,
               32:8,
               2:9,
               31:10,
               3:11,
               30:12},
}


kmap_soft = {
  'l1': {0:None, 1:None, 2:None},
  'l2': {0:None, 1:None, 2:None},
  'l3': {0:'2', 1:'2', 2:'0'},
  'l4': {0:'1', 1:'0', 2:'1'},
  'l5': {0:ecodes.KEY_A, 1:ecodes.KEY_J, 2:ecodes.KEY_9},
  'l6': {0:ecodes.KEY_E, 1:ecodes.KEY_P, 2:ecodes.KEY_0},
  'l7': {0:ecodes.KEY_F, 1:ecodes.KEY_G, 2:ecodes.KEY_MINUS},
  'l8': {0:ecodes.KEY_S, 1:ecodes.KEY_Q, 2:ecodes.KEY_EQUAL},
  'l9': {0:ecodes.KEY_C, 1:None, 2:None},
  'l10':{0:ecodes.KEY_I, 1:ecodes.KEY_B, 2:None},
  'l11':{0:ecodes.KEY_Y, 1:ecodes.KEY_SEMICOLON, 2:None},
  'l12':{0:ecodes.KEY_N, 1:ecodes.KEY_QUESTION, 2:None},
  'r1': {0:ecodes.KEY_ENTER, 1:None, 2:None},
  'r2': {0:ecodes.KEY_BACKSPACE, 1:None, 2:None},
  'r3': {0:ecodes.KEY_SPACE, 1:None, 2:None},
  'r4': {0:ecodes.KEY_LEFTSHIFT, 1:ecodes.KEY_LEFTSHIFT, 2:None},
  'r5': {0:ecodes.KEY_T, 1:ecodes.KEY_W, 2:ecodes.KEY_1},
  'r6': {0:ecodes.KEY_D, 1:ecodes.KEY_L, 2:ecodes.KEY_2},
  'r7': {0:ecodes.KEY_H, 1:ecodes.KEY_K, 2:ecodes.KEY_3},
  'r8': {0:ecodes.KEY_M, 1:ecodes.KEY_V, 2:ecodes.KEY_4},
  'r9': {0:ecodes.KEY_O, 1:ecodes.KEY_X, 2:ecodes.KEY_5},
  'r10':{0:ecodes.KEY_U, 1:ecodes.KEY_Z, 2:ecodes.KEY_6},
  'r11':{0:ecodes.KEY_R, 1:ecodes.KEY_COMMA, 2:ecodes.KEY_7},
  'r12':{0:ecodes.KEY_L, 1:ecodes.KEY_DOT, 2:ecodes.KEY_8} 
}

key_labels = {
  None: ('',),
  '0': (u'\u24ea',"u2400.woff"),
  '1': (u'\u2460',"u2400.woff"),
  '2': (u'\u2461',"u2400.woff"),
  '3': (u'\u2462',"u2400.woff"),
  '4': (u'\u2463',"u2400.woff"),
  '5': (u'\u2464',"u2400.woff"),
  '6': (u'\u2465',"u2400.woff"),
  '7': (u'\u2466',"u2400.woff"),
  '8': (u'\u2467',"u2400.woff"),
  ecodes.KEY_LEFTSHIFT: (u'\u21e7', "u2000.woff"),
  ecodes.KEY_APOSTROPHE: [('\"',"u0000.woff"),('\'',"u0000.woff")],
  ecodes.KEY_BACKSPACE: (u'\u232b',"ui-symbol.ttf"),
  ecodes.KEY_SPACE: (u'\u1680',"u1400.woff"),
  ecodes.KEY_QUESTION: [('?',"u0000.woff"),('/',"u0000.woff")],
  ecodes.KEY_COMMA:  [('<',"u0000.woff"),(',',"u0000.woff")],
  ecodes.KEY_DOT: [('>',"u0000.woff"),('.',"u0000.woff")], 
  ecodes.KEY_SEMICOLON: [(':',"u0000.woff"),(';',"u0000.woff")],
  ecodes.KEY_ENTER: (u'\u2386',"u2000.woff"),
  ecodes.KEY_MINUS:[('_',"u0000.woff"),('-',"u0000.woff")],
  ecodes.KEY_EQUAL:[('+',"u0000.woff"),('=',"u0000.woff")]
  }

def get_label(ecode):
    if ecode in key_labels:
      return key_labels[ecode]
    else:
      return ecodes.KEY[ecode][4:]

uinput  =  UInput()
mode = 0
while True:
    r, w, x = select(devices, [], [])
    for fd in r:
        for event in devices[fd].read():
          if event.type == ecodes.EV_KEY:
            device_name = devices[fd].name[-4:]
            device_hand = dmap[device_name]
            button_number = kmap_hard[device_hand][event.code]
            button_name = '{}{}'.format(device_hand, button_number)
            code = kmap_soft[button_name][mode]
            if type(code) == str and event.value < 2:
              mode = int(code)
        
            for k, v in kmap_soft.iteritems():
              ui.status[k]['label'] = get_label(v[mode])



            ui.status[button_name]['down'] = event.value
            ui.update()
            if type(code) is int:
              uinput.write(ecodes.EV_KEY, kmap_soft[button_name][mode], event.value)
              uinput.syn()
