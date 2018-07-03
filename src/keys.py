import evdev.ecodes as e

class Key(object):
    def __init__(self, code, symbol, modifiers=tuple()): 
        self.code = code
        self.symbol = symbol
        self.modifiers = modifiers
    
    def __repr__(self):
        return 'code:{}, symbol:{}, modifiers:{}'.format(
            self.code, self.symbol, self.modifiers)

class Mod(Key):
    pass

MOD_0 = Mod(0, (u'\u24ea',"u2400.woff"))
MOD_1 = Mod(1, (u'\u2460',"u2400.woff"))
MOD_2 = Mod(2, (u'\u2461',"u2400.woff"))
MOD_3 = Mod(3, (u'\u2462',"u2400.woff"))
MOD_4 = Mod(4, (u'\u2463',"u2400.woff"))
MOD_5 = Mod(4, (u'\u2464',"u2400.woff"))
MOD_6 = Mod(4, (u'\u2465',"u2400.woff"))
MOD_7 = Mod(4, (u'\u2466',"u2400.woff"))
MOD_8 = Mod(4, (u'\u2467',"u2400.woff"))

# first row
ESCAPE = Key(e.KEY_ESC, 'Esc')

F_1 = Key(e.KEY_F1, 'F1') 
MUTE = Key(e.KEY_MUTE, 'Mute')

F_2 = Key(e.KEY_F2, 'F2') 
VOLUME_DOWN = Key(e.KEY_VOLUMEDOWN, 'V Down')

F_3 = Key(e.KEY_F3, 'F3') 
VOLUME_UP = Key(e.KEY_VOLUMEUP, 'V up')

F_4 = Key(e.KEY_F4, 'F4') 

F_5 = Key(e.KEY_F5, 'F5') 

F_6 = Key(e.KEY_F6, 'F6') 

F_7 = Key(e.KEY_F7, 'F7') 

F_8 = Key(e.KEY_F8, 'F8') 

F_9 = Key(e.KEY_F9, 'F9') 

F_10 = Key(e.KEY_F10, 'F10') 

F_11 = Key(e.KEY_F11, 'F11') 

F_12 = Key(e.KEY_F12, 'F12') 

PRINT_SCREEN = Key(e.KEY_SCREEN , 'Print Screen')

INSERT = Key(e.KEY_INSERT, 'Insert')

DELETE = Key(e.KEY_DELETE , 'Delete')

# Row 2
TILDE = Key(e.KEY_APOSTROPHE, '~', ('shift',))
OPENING_APOSTROPHE = Key(e.KEY_APOSTROPHE, '`')

NUM_1 = Key(e.KEY_1, '1')
EXCLAMATION = Key(e.KEY_1, '!', ('shift',))

NUM_2 = Key(e.KEY_2, '2')
AT = Key(e.KEY_2, '@', ('shift',))

NUM_3 = Key(e.KEY_3, '3')
NUMBER_SIGN = Key(e.KEY_3, '3', ('shift',))

NUM_4 = Key(e.KEY_4, '4')
DOLLAR_SIGN = Key(e.KEY_4, '#', ('shift',))

NUM_5 = Key(e.KEY_5, '5')
PERCENTAGE_SIGN = Key(e.KEY_5, '%', ('shift',))

NUM_6 = Key(e.KEY_6, '6')
HAT_SIGN = Key(e.KEY_6, '^', ('shift',))

NUM_7 = Key(e.KEY_7, '7')
AMPERSAN_SIGN = Key(e.KEY_7, '&', ('shift',))

NUM_8 = Key(e.KEY_8, '8')
ASTERISK_SIGN = Key(e.KEY_8, '*', ('shift',))

NUM_9 = Key(e.KEY_9, '9')
OPENING_PARENTESIS = Key(e.KEY_9, '(', ('shift',))

NUM_0 = Key(e.KEY_0, '0')
CLOSING_PARENTESIS = Key(e.KEY_0, ')', ('shift',))

MINUS_SIGN = Key(e.KEY_MINUS, ('-',"u0000.woff"))
UNDERSCORE = Key(e.KEY_MINUS, ('_',"u0000.woff"), ('shift',))

EQUAL_SIGN = Key(e.KEY_EQUAL, ('=',"u0000.woff"))
PLUS_SIGN = Key(e.KEY_EQUAL, ('+',"u0000.woff"), ('shift',))

BACKSPACE = Key(e.KEY_BACKSPACE, (u'\u232b',"ui-symbol.ttf"))

# Row 3
TAB = Key(e.KEY_TAB, 'Tab')

LOWER_Q = Key(e.KEY_Q, 'q')
UPPER_Q = Key(e.KEY_Q, 'Q', ('shift',))

LOWER_W = Key(e.KEY_W, 'w')
UPPER_W = Key(e.KEY_W, 'W', ('shift',))

LOWER_E = Key(e.KEY_E, 'e')
UPPER_E = Key(e.KEY_E, 'E', ('shift',))

LOWER_R = Key(e.KEY_R, 'r')
UPPER_R = Key(e.KEY_R, 'R', ('shift',))

LOWER_T = Key(e.KEY_T, 't')
UPPER_T = Key(e.KEY_T, 'T', ('shift',))

LOWER_Y = Key(e.KEY_Y, 'y')
UPPER_Y = Key(e.KEY_Y, 'Y', ('shift',))


LOWER_U = Key(e.KEY_U, 'u')
UPPER_U = Key(e.KEY_U, 'U', ('shift',))

LOWER_I = Key(e.KEY_I, 'i')
UPPER_I = Key(e.KEY_I, 'I', ('shift',))

LOWER_O = Key(e.KEY_O, 'o')
UPPER_O = Key(e.KEY_O, 'O', ('shift',))

LOWER_P = Key(e.KEY_P, 'p')
UPPER_P = Key(e.KEY_P, 'P', ('shift',))

# Row 4
LOWER_A = Key(e.KEY_A, 'a')
UPPER_A = Key(e.KEY_A, 'A', ('shift',))

LOWER_S = Key(e.KEY_S, 's')
UPPER_S = Key(e.KEY_S, 'S', ('shift',))

LOWER_D = Key(e.KEY_D, 'd')
UPPER_D = Key(e.KEY_D, 'D', ('shift',))

LOWER_F = Key(e.KEY_F, 'f')
UPPER_F = Key(e.KEY_F, 'F', ('shift',))

LOWER_G = Key(e.KEY_G, 'g')
uPPER_G = Key(e.KEY_G, 'G', ('shift',))

LOWER_H = Key(e.KEY_H, 'h')
UPPER_H = Key(e.KEY_H, 'H', ('shift',))

LOWER_J = Key(e.KEY_J, 'j')
UPPER_J = Key(e.KEY_J, 'J', ('shift',))

LOWER_K = Key(e.KEY_K, 'k')
UPPER_K = Key(e.KEY_K, 'K', ('shift',))

LOWER_L = Key(e.KEY_L, 'l')
UPPER_L = Key(e.KEY_L, 'L', ('shift',))

SEMICOLON = Key(e.KEY_SEMICOLON, ':')
COLON  = Key(e.KEY_SEMICOLON, ':', ('shift',))

ENTER = Key(e.KEY_ENTER, 'Enter')

# Row 5
LOWER_Z = Key(e.KEY_Z, 'z')
UPPER_Z = Key(e.KEY_Z, 'Z', ('shift',))

LOWER_X = Key(e.KEY_X, 'x')
UPPER_X = Key(e.KEY_X, 'X', ('shift',))

LOWER_C = Key(e.KEY_C, 'c')
UPPER_C = Key(e.KEY_C, 'C', ('shift',))

LOWER_V = Key(e.KEY_V, 'v')
UPPER_V = Key(e.KEY_V, 'V', ('shift',))

LOWER_B = Key(e.KEY_B, 'b')
UPPER_B = Key(e.KEY_B, 'B', ('shift',))

LOWER_N = Key(e.KEY_N, 'n')
UPPER_N = Key(e.KEY_N, 'N', ('shift',))

LOWER_M = Key(e.KEY_M, 'm')
UPPER_M = Key(e.KEY_M, 'M', ('shift',))





SPACE = Key(e.KEY_SPACE, (u'\u1680',"u1400.woff"))

SLASH =  Key(e.KEY_SLASH, ('?',"u0000.woff"))
QUESTION_MARK =  Key(e.KEY_SLASH, ('?',"u0000.woff"), ('shift',))

DOT = Key(e.KEY_DOT, ('.',"u0000.woff"))
CLOSE_ANGULAR_BRAKET = Key(e.KEY_DOT, ('>',"u0000.woff"), ('shift',))

code = [
      [MOD_1,       MOD_1,          MOD_1,      MOD_1, MOD_1],
      [MOD_2,       MOD_2,          MOD_2,      MOD_2, MOD_2],
      [MOD_3,       MOD_3,          MOD_3,      MOD_3, MOD_3],
      [MOD_4,       MOD_4,          MOD_4,      MOD_4, MOD_4],
      [LOWER_A,     LOWER_J,        NUM_9,      F_9,    DOT],
      [LOWER_E,     LOWER_P,        NUM_0,      F_10,   DOT],
      [LOWER_F,     LOWER_G,        MINUS_SIGN, F_11,   DOT],
      [LOWER_S,     LOWER_Q,        EQUAL_SIGN, F_12,   DOT],
      [LOWER_C,     LOWER_K,        DOT,        DOT,    DOT],
      [LOWER_I,     LOWER_B,        DOT,        DOT,    DOT],
      [LOWER_Y,     SEMICOLON,      DOT,        DOT,    DOT],
      [LOWER_N,     QUESTION_MARK,  DOT,        DOT,    DOT],

      [ENTER,       DOT,            DOT,        DOT,    DOT],
      [BACKSPACE,   DOT,            DOT,        DOT,    DOT],
      [SPACE,       DOT,            DOT,        DOT,    DOT],
      [DOT,         DOT,            DOT,        DOT,    DOT],
      [LOWER_T,     LOWER_W,        NUM_1,      F_1,    MUTE],
      [LOWER_D,     LOWER_L,        NUM_2,      F_2,    VOLUME_DOWN],
      [LOWER_H,     LOWER_K,        NUM_3,      F_3,    VOLUME_UP],
      [LOWER_M,     LOWER_V,        NUM_4,      F_4,    DOT],
      [LOWER_O,     LOWER_X,        NUM_5,      F_5,    DOT],
      [LOWER_U,     LOWER_Z,        NUM_6,      F_6,    DOT],
      [LOWER_R,     LOWER_Z,        NUM_7,      F_8,    DOT],
      [LOWER_L,     DOT,            NUM_8,      F_8,    DOT] 
    ]





