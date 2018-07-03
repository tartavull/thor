"""
run me like:
sudo env "PATH=$PATH" ipython --pdb linux.py
"""
from __future__ import print_function, absolute_import, division

import os
import re
from select import select

from evdev import InputDevice, ecodes, UInput

import ui
import keys

def get_device_names():
    #import bluetooth
    #FIXME bluetooth low energy scan
    #for address, name in DiscoveryService().discover(2).tems():
    #    print("name: {}, address: {}".format(name, address))
    return ['a403','a496']

def get_event_id(device_name):
    command = 'cat /proc/bus/input/devices'
    stdout = os.popen(command).read()
    regex = r'Name=".*{}"\n.*\n.*\n.*\nH: Handlers=.*event(\d*)'.format(device_name)
    return re.findall(regex, stdout)[0]

def get_xinput_id(device_name):
    """
    Returns the event id for the keyboard with this name.
    """
    command = 'xinput list --long | grep keyboard | grep {}'.format(device_name)
    stdout = os.popen(command).read()
    return int(re.findall(r'id=(\d+)', stdout)[0])

def get_event_file(event_id):
    return  '/dev/input/event{}'.format(event_id)

def get_input_devices():
    for name in get_device_names():
        event_path = get_event_file(get_event_id(name))
        dev = InputDevice(event_path)
        dev.grab()
        yield dev.fd, dev

def get_device_hand(device_name):
    return {'a403':'r', 'a496':'l'}[device_name]

def get_device_button(device_name, event_code):
    """
    The wires were connected on abitrary postions onto
    the board, this maps goes from the code the keyboard
    emmitted to the postion on the device.
    """
    return { 'a403': [28, 2, 106, 57, 103, 3, 108, 17, 105, 30, 31, 32],
             'a496': [108, 17, 103, 57, 105, 28, 106, 32, 2, 31, 3, 30],
     }[device_name].index(event_code)

def get_mapped_key(button, modifier):
    return keys.code[button][modifier]   

class VirtualKeyboard(object):
    
    def __init__(self):
        self._uinput = UInput()
        self._modifier = 0

    def apply_key(self, key):
        if 'shift' in key.modifiers:
            self._uinput.write(ecodes.EV_KEY, ecodes.KEY_LEFTSHIFT, 1)

        self._uinput.write(ecodes.EV_KEY, key.code, 1)
        self._uinput.write(ecodes.EV_KEY, key.code, 0)
        
        if 'shift' in key.modifiers:
            self._uinput.write(ecodes.EV_KEY, ecodes.KEY_LEFTSHIFT, 0)
        self._uinput.syn()

active_keys = set()
def process_key_event(virtual_keyboard, event, device_name):
    device_button = get_device_button(device_name, event.code)
    if get_device_hand(device_name) == 'r':
        device_button += 12        
    key = get_mapped_key(device_button, virtual_keyboard._modifier)
    
    if event.value == 1:
        #key pressed
        active_keys.add(device_button)
        if type(key) is keys.Key:
            virtual_keyboard.apply_key(key)
        else:
            virtual_keyboard._modifier = key.code
    elif event.value == 0:
        #key released
        active_keys.remove(device_button)
        if type(key) is keys.Mod:
            virtual_keyboard._modifier = 0

    elif event.value == 2:
        #key held down
        return

    mapping = [get_mapped_key(b, virtual_keyboard._modifier) for b in range(24)]
    ui.update(mapping, active_keys)


def start_event_loop(devices):
    vk = VirtualKeyboard()
    while True:
        to_read, _, _ = select(devices, [], [])
        for fd in to_read:
            for event in devices[fd].read():
                if event.type != ecodes.EV_KEY:
                    continue
                device_name = devices[fd].name[-4:]
                process_key_event(vk, event, device_name)

if __name__ == '__main__':
    devices =  dict(get_input_devices())
    start_event_loop(devices)
