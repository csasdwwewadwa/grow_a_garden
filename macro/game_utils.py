import pyautogui as pag

import csamacro
from ahk_utils import *

def is_disconnected():
    return pag.pixel(1100, 429) == (57, 59, 61)


def rotate_camera(x, y):
    CAMERA_SENSITIVITY = 0.5
    csamacro.mouse_move_absolute(1500, 115)
    csamacro.mouse_move_relative(0, 5)
    csamacro.mouse_move_relative(0, -5)
    csamacro.mouse_button_down('right')
    csamacro.mouse_button_up('right')
    csamacro.mouse_move_relative(0, 5)
    csamacro.mouse_button_down('right')
    csamacro.mouse_move_relative(round(x/CAMERA_SENSITIVITY*2), round(-y/CAMERA_SENSITIVITY*2), debounce=0.1)
    csamacro.mouse_button_up('right')
    csamacro.mouse_move_absolute(1500, 115)


def get_weather():
    def is_thunderstorm():
        return pag.pixel(1888, 997) == (255, 255, 127)

    def is_blizzard():
        return pag.pixel(1890, 1001) == (123, 233, 255)

    def is_rain():
        return pag.pixel(1890, 1007) == (0, 170, 255)
    
    if is_thunderstorm():
        return 'thunderstorm'
    elif is_blizzard():
        return 'blizzard'
    elif is_rain():
        return 'rain'
    else:
        return None

def tp_seed():
    click_wait(679, 137)

def get_egg_rarity():
    if pag.pixel(798, 366) == (255, 255, 255):
        return 'common'
    elif pag.pixel(798, 360) == (211, 167, 129):
        return 'uncommon'
    elif pag.pixel(799, 367) == (33, 84, 185):
        return 'rare'
    elif pag.pixel(798, 360) == (213, 255, 134):
        return 'bug'
    else:
        return 'unknown'

def setup_camera():
    tp_seed()
    time.sleep(0.3)
    rotate_camera(0, -1000) # to top_down
    csamacro.mouse_scroll(-25) # zoom all out
    csamacro.mouse_scroll(5, debounce=0.3) # zoom in a bit
    
    # check for default camera position
    pxr = pag.pixel(1714, 628)
    pxl = pag.pixel(270, 628)
    pxur = pag.pixel(1509, 258)
    pxul = pag.pixel(407, 158)

    # case 1: 90
    if pxr[1] - pxr[2] < 70:
        rotate_camera(90, 0)
    
    # case 2: -90
    elif pxl[1] - pxl[2] < 70:
        rotate_camera(-90, 0)

    # case 3: 30.5
    elif pxur[1] - pxur[2] < 70:
        rotate_camera(30.5, 0)

    # case 4: -30.5
    elif pxul[1] - pxul[2] < 70:
        rotate_camera(-30.5, 0)
            
def setup_shops():
    # move to gear shop thing
    ahk.key_press('shift')
    key_hold('s', 17)
    ahk.key_press('shift')

    # prepare gear shop ui
    ahk.key_press('e')
    time.sleep(4)
    ahk.mouse_move(1027, 518)
    ahk.click(1090, 518)
    time.sleep(2) # wait for shop ui

    # snap to rod
    for _ in range(4):
        ahk.mouse_move(733, 873)
        click_wait(987, 873)

    ahk.click(1288, 264) # close diag
