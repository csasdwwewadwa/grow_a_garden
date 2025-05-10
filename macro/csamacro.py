'''
Low level keyboard + mouse control for windows cuz PRO
Yayers
'''


import ctypes
import time

# Constants from WinUser.h
INPUT_MOUSE = 0

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010

MOUSEEVENTF_WHEEL = 0x0800
WHEEL_DELTA = 120

# Defaults
DEFAULT_DEBOUNCE_TIME = 0.05


# Bake constants
screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)


# Structures
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong), # For MOUSEEVENTF_WHEEL, this is the wheel delta (signed).
                                       # ctypes handles conversion from Python int to c_ulong.
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
    ]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("mi", MOUSEINPUT)]
    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_ulong), ("_input", _INPUT)]

SendInput = ctypes.windll.user32.SendInput



def mouse_move_relative(x, y, debounce=DEFAULT_DEBOUNCE_TIME):
    mi = MOUSEINPUT(dx=x, dy=y, 
                    mouseData=0, 
                    dwFlags=MOUSEEVENTF_MOVE, 
                    time=0, 
                    dwExtraInfo=None)
    inp = INPUT(type=INPUT_MOUSE, mi=mi)
    SendInput(1, ctypes.pointer(inp), ctypes.sizeof(inp))
    time.sleep(debounce)

def mouse_move_absolute(x, y, debounce=DEFAULT_DEBOUNCE_TIME):
    abs_x = int(x * 65535 / screen_width)
    abs_y = int(y * 65535 / screen_height)

    mi = MOUSEINPUT(dx=abs_x, dy=abs_y, 
                    mouseData=0,
                    dwFlags=MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE,
                    time=0, 
                    dwExtraInfo=None)
    inp = INPUT(type=INPUT_MOUSE, mi=mi)
    SendInput(1, ctypes.pointer(inp), ctypes.sizeof(inp))
    time.sleep(debounce)

def mouse_button_down(button="left", debounce=DEFAULT_DEBOUNCE_TIME):
    flags = MOUSEEVENTF_LEFTDOWN if button == "left" else MOUSEEVENTF_RIGHTDOWN
    mi = MOUSEINPUT(dx=0, dy=0, 
                    mouseData=0, 
                    dwFlags=flags, 
                    time=0, 
                    dwExtraInfo=None)
    inp = INPUT(type=INPUT_MOUSE, mi=mi)
    SendInput(1, ctypes.pointer(inp), ctypes.sizeof(inp))
    time.sleep(debounce)

def mouse_button_up(button="left", debounce=DEFAULT_DEBOUNCE_TIME):
    flags = MOUSEEVENTF_LEFTUP if button == "left" else MOUSEEVENTF_RIGHTUP
    mi = MOUSEINPUT(dx=0, dy=0, 
                    mouseData=0, 
                    dwFlags=flags, 
                    time=0, 
                    dwExtraInfo=None)
    inp = INPUT(type=INPUT_MOUSE, mi=mi)
    SendInput(1, ctypes.pointer(inp), ctypes.sizeof(inp))
    time.sleep(debounce)

def mouse_scroll(n=1, debounce=DEFAULT_DEBOUNCE_TIME):
    mouse_data_value = WHEEL_DELTA
    if n < 0:
        n = -n
        mouse_data_value = -mouse_data_value
    
    mi = MOUSEINPUT(dx=0, dy=0, 
                    mouseData=mouse_data_value, 
                    dwFlags=MOUSEEVENTF_WHEEL, 
                    time=0, 
                    dwExtraInfo=None)
    
    inp = INPUT(type=INPUT_MOUSE, mi=mi)
    for _ in range(n):
        SendInput(1, ctypes.pointer(inp), ctypes.sizeof(inp))
        time.sleep(debounce)


def mouse_drag(from_pos, to_pos, button='left', debounce=DEFAULT_DEBOUNCE_TIME):
    mouse_move_absolute(*from_pos, debounce=debounce)
    mouse_button_down(button, debounce=debounce)
    mouse_move_absolute(*to_pos, debounce=debounce)
    mouse_button_up(button, debounce=debounce)